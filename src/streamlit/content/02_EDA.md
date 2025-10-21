### Pertinence

Dans le cadre de cette étude visant à classifier des cellules sanguines à partir d’images de microscopie à l’aide de techniques de Deep Learning et de traitement d’image avec OpenCV, plusieurs éléments du jeu de données apparaissent particulièrement pertinents.

#### Variables pertinentes au regard des objectifs

L’objectif principal étant la classification des cellules en différentes catégories (par exemple : neutrophiles, éosinophiles, lymphocytes, monocytes), la variable la plus informative est naturellement l’image elle-même. Chaque image contient des informations morphologiques essentielles que les modèles convolutionnels peuvent apprendre à exploiter.
Les métadonnées associées (par exemple le nom de la classe) sont également importantes pour l’étiquetage supervisé.

#### Variable cible

La variable cible est la classe de la cellule représentée sur l’image, c’est-à-dire son type (exemple: ‘neutrophil’, ‘eosinophil’, ‘lymphocyte’, ‘monocyte’). Cette variable est catégorielle et sert de référence pour entraîner le modèle de classification.

#### Particularités du jeu de données

Le jeu de données présente plusieurs caractéristiques notables :

- Format légèrement hétérogène : les images ont une dimensions de 360x363 pixels à de rares exceptions,
- Diversité des classes : le dataset comporte plusieurs types de cellules, ce qui permet d’entraîner un modèle multi-classe,
- Structure arborescente claire : les images sont regroupées dans des répertoires par classe, ce qui facilite leur utilisation avec des modèles TensorFlow ou Keras.

![Types cellulaires](src/streamlit/assets/cell_types.png)
**Figure 2.** Exemples des différents types cellulaires représentés dans le jeu de données.

#### Limitations des données

Quelques limitations doivent être prises en compte :

- Déséquilibre entre classes : certaines classes sont sur- ou sous-représentées, ce qui pourrait biaiser l’apprentissage du modèle,
- Variabilité des conditions d’acquisition : les images proviennent de sources ou de microscopes différents, cela peut introduire un bruit non contrôlé.

---

### Pre-processing et feature engineering

#### Nettoyage des données

Une phase de nettoyage des données a été nécessaire afin d'éliminer les données non disponibles (fichier corrompu) et les valeurs aberrantes (outliers) :

- **Données non disponibles**: 1 seul fichier corrompu a été identifié et supprimé,
- **Valeurs aberrantes**: 214 fichiers ont été supprimés sur la base du flou, de l'exposition ou du contraste.

#### Feature engineering (Décentrage des images)

Afin de garantir que le modèle d'apprentissage ne développe pas une dépendance à la position centrale des cellules dans les images, nous avons appliqué un décentrage systématique des images du dataset. Cette étape vise à éviter que le modèle ne sur-apprenne des biais liés à la localisation des cellules, en s'assurant qu'il se concentre sur les caractéristiques morphologiques pertinentes plutôt que sur leur position dans le cadre. Ce décentrage a été réalisé en combinant des translations aléatoires sur les axes X et Y, tout en maintenant les cellules visibles dans l'image. Cette approche contribue à améliorer la robustesse et la généralisation du modèle lors de la phase de prédiction.

![Décentrage des images](src/streamlit/assets/decentered.png)
**Figure 3.** Décentrage des images du jeu de données.

#### Traitement des données

Une phase de prétraitement des données a été nécessaire afin d’assurer une meilleure qualité d’apprentissage pour le modèle. Les images ont été :

- **Redimensionnées** à une taille uniforme de 224x224 pixels pour assurer la compatibilité avec les architectures de réseaux de neurones convolutionnels standard,
- **Converties en niveaux de gris**, ce qui permet de réduire la complexité des données tout en conservant les principales informations morphologiques nécessaires à la classification,
- **Filtrées à l’aide du filtre Laplacien** (OpenCV) afin d’accentuer les bords et les contours cellulaires, facilitant ainsi l’extraction automatique de caractéristiques discriminantes par le réseau.

![Taille des images](src/streamlit/assets/image_sizes.png)
**Figure 4.** Répartition des tailles des images du jeu de données.

#### Normalisation / standardisation

Une normalisation des données a été appliquée. Les pixels des images, initialement encodés sur 8 bits (valeurs entre 0 et 255), ont été **normalisés dans l’intervalle [0, 1]**.

![Pré-traitement](src/streamlit/assets/preprocessing.png)
**Figure 5.** Étapes de pré-traitement appliquées au jeu de données (redimensionnement, niveaux de gris, Laplacienne).

#### Réduction de dimension

À ce stade du projet, aucune technique de réduction de dimension (comme PCA ou t-SNE) n’a été appliquée avant la phase de modélisation. Toutefois, ces techniques pourraient être envisagées ultérieurement dans une approche de modélisation de machine learning classique.

---

### Visualisations et Statistiques

#### Relations entre variables

Dans le cadre de ce projet, la variable explicative principale est l’image prétraitée, et la variable cible est la classe cellulaire (neutrophile, éosinophile, lymphocyte, monocyte). Les relations classiques entre variables tabulaires n’existent donc pas ici.

Les caractéristiques morphologiques extraites automatiquement par un CNN devront donc avoir un fort potentiel discriminant.

#### Distribution des données

Une analyse de la répartition des images par classe a été menée :

- Des images floues (outliers) ont été repérées et supprimées.
  ![Cell types](src/streamlit/assets/outliers.png)
  **Figure 6.** Exemples des différents types cellulaires représentés dans le jeu de données.

- Déséquilibre modéré entre les classes, certaines étant plus représentées que d’autres (par exemple, les neutrophiles sont plus nombreux que les éosinophiles). Nous avons généré des images par retournement et/ou rotation afin d'obtenir des classes équilibrées.
  ![Répartition des classes](src/streamlit/assets/cell_types_proportion.png)
  **Figure 7.** Répartition des différentes classes cellulaires dans le jeu de données initial.

#### Analyses statistiques utilisées

Plusieurs analyses simples ont été menées :

- Histogrammes de répartition par classe pour identifier les déséquilibres,
- Moyenne et écart-type des intensités de pixels pour vérifier l’homogénéité des images.

#### Conclusions pour la modélisation

Les éléments ci-dessus suggèrent que le prétraitement des images est adéquat pour une entrée dans un réseau convolutionnel.
