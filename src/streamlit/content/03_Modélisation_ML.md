### Pre-processing et featuring

#### Nettoyage et contrôle qualité

Plusieurs étapes ont été réalisées afin d’assurer la qualité et l’homogénéité du jeu de données :

- **Détection et suppression des doublons** : utilisation d’un **hashing perceptuel** (hash MD5 appliqué sur les images) permettant d’identifier les images identiques ou quasi-identiques, **17 doublons** ont été retirés.
- **Suppression des outliers** : exclusion d’images floues, surexposées ou très bruitées, identifiées manuellement et par seuil sur la variance. **214 images** ont été supprimées.
- **Nettoyage des fichiers corrompus** : un fichier inutilisable a été écarté.

Ces étapes garantissent que le dataset final ne contient pas d’exemples redondants ou trompeurs qui pourraient biaiser l’entraînement.

#### Extraction de features (24 variables)

À partir des images pré-traitées (redimensionnement, niveaux de gris, accentuation des bords – cf. Rendu 1), nous extrayons un vecteur compact de **24** variables par image :

- **Statistiques d’intensité** : moyenne, écart-type, minimum, maximum, médiane, variance,
- **Distribution** : **kurtosis** (aplatissement),
- **Énergie** (somme des intensités au carré),
- **Histogramme 16 bins** des niveaux de gris (normalisé).

#### Décentrage (data augmentation géométrique légère)

Afin de limiter la dépendance à la position centrale des cellules, nous appliquons un **décentrage aléatoire** (translations via `warpAffine`) sur les images d’entraînement. En plus d'appliquer ce décentrage, pour ré-équilibrer les classes nous faisons une partie overfitting en appliquant des fonction de transformation d'image (rotation, flip, ...).

#### Découpage, équilibrage et tailles

##### Jeu de données pour les 13 classes

- **Split** : jeu d’entraînement / test.
- **Après décentrage et équilibrage** : `X_train` est de **(16 365, 24)** à ; `y_train` : **16 365**.

##### Jeu de test pour les 8 classes

- **Split** : jeu d’entraînement / test.
- **Après décentrage et équilibrage** : `X_train` est de **(26 976, 21)** à ; `y_train` : **26 976**.

#### Réduction de dimension (LDA (13 classes) et PCA (8 classes))

Nous appliquons une **Analyse Discriminante Linéaire (LDA)** sur la préparation à 13 classes pour projeter les features dans un espace réduit à de dimension **12**, ce qui devrait permettre de mieux différencier les classes : `X_train_lda` : **(16 365, 12)**, `X_test_lda` : **(3 415, 12)**.

Nous appliquons une **Principal Composant Analysis (PCA)** sur la préparation à 8 classes pour projeter les features dans un espace réduit a dimension **10**, ce qui devrait permettre de mieux différencier les classes : `X_train_pca` : **(26 976, 10)**, `X_test_lda` : **(26 976, 10)**.

---

### Modèles testés et réglages

Différent modèle ont été testé sur les deux jeux de données. Pour les 8 classes les modèles testés sont : RandomForest, SVC, KNeighborsClassifier et XGBoost. Pour la le jeu de données à 13 classes les modèle testés sont RandomForest et SVC.

---

### Résultat globaux

Les différents modèles testés sur la préparation à 8 classes ont eu des résultats plutôt moyens. Le moins bon étant SVC avec une accuracy de 0.59 et le moins bon étant KNeighborsClassifier avec une ccuracy de 0.50.
Pour la préparation à 13 classes les résultats sont légèrement meilleurs, avec une accuraccy la plus élevée pour le modèle SVC à 0.79 contre 0.76 pour le RandomForest.

Pour modèles testés sur 8 classes, les plus diffciles à identifier sont les basophil, eosinophil, lymphocyte et ig avec des confusions croisées visibles dans les matrices.
Pour modèles testés sur 13 classes, les plus diffciles à identifier sont les MMY, PMY et MY.

Dans la suite nous présenterons les résultats du modèle ayant eu les meilleurs performances.

#### SVC (RBF)

#### Classification Report

| Classe       | Precision | Recall | F1-score | Support |
| ------------ | --------- | ------ | -------- | ------- |
| BNE          | 0.62      | 0.60   | 0.61     | 327     |
| MMY          | 0.40      | 0.36   | 0.38     | 203     |
| MY           | 0.51      | 0.51   | 0.51     | 227     |
| PMY          | 0.63      | 0.66   | 0.64     | 118     |
| SNE          | 0.69      | 0.73   | 0.71     | 329     |
| basophil     | 0.85      | 0.93   | 0.89     | 242     |
| eosinophil   | 0.94      | 0.93   | 0.94     | 622     |
| erythroblast | 0.95      | 0.88   | 0.91     | 310     |
| ig           | 0.71      | 0.97   | 0.82     | 30      |
| lymphocyte   | 0.86      | 0.88   | 0.87     | 243     |
| monocyte     | 0.78      | 0.77   | 0.77     | 284     |
| neutrophil   | 1.00      | 0.70   | 0.82     | 10      |
| platelet     | 1.00      | 0.99   | 0.99     | 470     |

**Tableau 1.** Performances du modèle **SVC (RBF)** sur le jeu de test (features LDA, 13 classes).

#### Global Metrics

![Matrice de confusion SVC](src/streamlit/assets/CONFUSION_MATRIX_SVM.png)
**Figure 8.** Matrice de confusion pour le modèle SVC (issue du notebook `nb_3_1_ml_SVM`).

- **Accuracy**: `0.79` (3415 samples)
- **Macro avg**: Precision = `0.76`, Recall = `0.76`, F1-score = `0.76`
- **Weighted avg**: Precision = `0.79`, Recall = `0.79`, F1-score = `0.79`

---

### Analyse et observations

- **Performance globale** : le SVC (RBF) atteint une **macro-F1** de **0.79**
- **Classes bien maîtrisées** : **eosinophil**, **erythroblast**, **platelet** (> 0.90 F1)
- **Points de fragilité** : les stades **immatures** (**BNE, MMY, MY, PMY**) restent plus difficiles (F1 ≈ 0.38–0.64), avec des confusions croisées visibles dans les matrices (ex. **BNE ↔ MY**, **MMY ↔ PMY**).
- **Effet du pipeline** : l’équilibrage + la LDA (12 dims) facilitent la séparation et permet de stabiliser l’entraînement.

---

### Conclusion et transition vers le Deep Learning

Ces expériences **Machine Learning** fournissent une ligne de base robuste : **accuracy ~0.79** sur 13 classes avec des features **hand-crafted** (statistiques + histogrammes) qui permettent de capturer une partie de la morphologie.

Cependant cela reste **moins expressif** que des _features_ apprises automatiquement en **vision** (CNN).

Et les difficultés persistantes sur les **stades immatures** et la **variabilité intra-classe** motivent l’pprentissage de représentations à partir des **pixels** via des **CNN** (Rendu 3), avec data augmentation ciblée, fine-tuning et interprétabilité (Grad-CAM).
