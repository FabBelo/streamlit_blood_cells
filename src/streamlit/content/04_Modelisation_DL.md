## Modélisation par Deep Learning

### Classification du problème

#### Type de problème de machine learning

Le projet relève d’une classification supervisée multi-classes visant à attribuer à chaque image de cellule sanguine un type précis. Le dataset, organisé en huit classes principales, couvre les neutrophiles, éosinophiles, basophiles, lymphocytes, monocytes, granulocytes immatures, érythroblastes et plaquettes. L’examen de la nomenclature a révélé treize sous-classes plus fines, mais leur faible représentation rendait l’apprentissage instable. Après plusieurs essais, la classification en huit classes a été retenue comme approche la plus robuste et la plus équilibrée, offrant un compromis entre granularité biologique et stabilité du modèle. Cette formulation constitue un cadre fiable pour l’apprentissage de modèles CNN capables de reconnaître les principales catégories cellulaires à partir d’images microscopiques.

#### Tâche de machine learning ciblée

La tâche correspond à une reconnaissance d’images médicales appliquée à des frottis sanguins d’individus sains. Le but est d’identifier le type cellulaire sans dimension diagnostique : il ne s’agit pas de détecter des maladies, mais d’apprendre les morphologies normales des cellules. Cette approche permet de tester la performance de différents réseaux convolutionnels sur des données homogènes et bien annotées, sans biais cliniques. Le projet s’apparente donc à un benchmark de classification d’images biomédicales où la qualité d’annotation et la précision de reconnaissance sont les critères essentiels. La nature standardisée du dataset offre un terrain idéal pour évaluer la capacité de généralisation des architectures profondes.

#### Métrique principale de performance et justification

La précision globale (accuracy) a été utilisée comme métrique principale d’évaluation. Elle mesure la proportion d’images correctement classées et constitue un indicateur simple et pertinent pour ce type de tâche. Ce choix est justifié par la distribution relativement équilibrée des classes, qui rend cette métrique représentative des performances réelles du modèle. L’accuracy est également courante dans les benchmarks de vision par ordinateur, facilitant ainsi la comparaison avec d’autres travaux publiés.

#### Autres métriques utilisées (qualitatives et/ou quantitatives)

En complément, le F1-score macro a permis de mieux évaluer les performances par classe en pondérant équitablement chaque catégorie, y compris les moins représentées. Cette métrique met en évidence les cellules plus difficiles à distinguer et aide à identifier les biais éventuels du modèle. L’analyse des précisions et rappels par classe a apporté des indications précieuses pour ajuster le pipeline de prétraitement et la stratégie d’entraînement. Enfin, la matrice de confusion a joué un rôle central pour visualiser les erreurs, notamment les confusions entre classes morphologiquement proches comme les neutrophiles et les granulocytes immatures, orientant ainsi les améliorations futures.

---

### Choix du modèle et optimisation

#### Algorithmes testés

Plusieurs architectures de réseaux de neurones convolutionnels ont été testées à l’aide de TensorFlow/Keras en s’appuyant sur le transfer learning à partir de modèles pré-entraînés sur ImageNet. L’objectif était d’évaluer différentes approches tout en garantissant leur pertinence pour un dataset biologique d’environ dix-sept mille images réparties en huit classes. Trois modèles ont servi de base : **VGG16**, choisi comme baseline robuste et simple à entraîner ; **DenseNet201**, permettant une meilleure réutilisation des caractéristiques grâce à ses connexions denses ; et **EfficientNetB0**, architecture plus moderne optimisée pour offrir le meilleur compromis entre performances et complexité. Ces modèles couvrent ainsi un spectre allant de la simplicité à l’efficacité computationnelle, permettant une comparaison équilibrée selon les contraintes du projet.

#### Modèles retenus et justification

Le modèle **VGG16** a servi de référence initiale. Sa simplicité et sa rapidité d’entraînement en font une baseline idéale, mais son architecture plus ancienne limite la finesse de reconnaissance morphologique. **DenseNet201**, en revanche, exploite ses connexions internes pour améliorer la propagation du gradient et capturer des détails subtils comme les contours nucléaires ou les granulations cytoplasmiques. Grâce à un fine-tuning partiel, il a permis de mieux différencier les classes proches, au prix d’un temps d’entraînement plus long. Enfin, **EfficientNetB0** s’est distingué par son rapport performance/poids exceptionnel. Son entraînement, enrichi de techniques de régularisation avancées telles que le label smoothing, le Dropout et l’optimiseur AdamW, a renforcé sa robustesse. Ce modèle, accompagné d’une analyse d’explicabilité via Grad-CAM, a montré une bonne capacité à localiser les régions clés des cellules. En somme, VGG16 constitue une référence rapide, DenseNet201 une approche performante, et EfficientNetB0 le meilleur compromis entre efficacité, stabilité et explicabilité.

#### Optimisation des hyperparamètres

Le pipeline d’entraînement a reposé sur un prétraitement rigoureux et un découpage reproductible du dataset. Les images corrompues ont été éliminées et les classes réorganisées pour obtenir un équilibre correct entre les huit catégories principales. Afin de pallier les déséquilibres persistants, une stratégie d’oversampling associée à de la data augmentation a été mise en œuvre. Les transformations appliquées - rotations, flips, translations et ajustements de luminosité - ont permis de diversifier les données tout en préservant la plausibilité biologique des images. Les hyperparamètres ont été harmonisés entre les modèles, avec une taille de lot de 32, une optimisation par Adam (ou AdamW pour EfficientNetB0), une perte de type categorical crossentropy et des entraînements de quinze à vingt-cinq epochs selon les architectures. Cette configuration a permis d’assurer la comparabilité entre les modèles tout en limitant le sur-apprentissage.

La comparaison finale montre que VGG16 offre une performance correcte et stable, mais reste limitée. DenseNet201 améliore sensiblement la reconnaissance des classes morphologiquement proches, tandis qu’EfficientNetB0 atteint un équilibre optimal entre précision, efficacité et robustesse. En fonction des besoins, VGG16 convient pour des expérimentations rapides, DenseNet201 pour la performance brute, et EfficientNetB0 pour une utilisation équilibrée et explicable.

#### Expérimentations avancées et motivation

L’essentiel du projet repose sur le deep learning par transfer learning et fine-tuning, stratégie justifiée par la richesse morphologique des images et la qualité d’annotation du dataset. Les approches classiques de bagging ou de boosting, bien que testées, se sont révélées moins adaptées à la nature visuelle du problème, où la feature learning automatique des CNN est bien plus efficace que les méthodes à caractéristiques manuelles. Des ensembles de modèles (ensembling) ont été envisagés pour un gain marginal de performance, mais leur complexité computationnelle ne justifiait pas leur intégration finale. Enfin, une piste d’évolution prometteuse consisterait à adopter une classification hiérarchique permettant de distinguer d’abord les grandes familles cellulaires avant de spécialiser la reconnaissance, ou à recourir à des techniques de metric learning pour améliorer la séparation des sous-types proches. Ces approches pourraient ouvrir la voie à une classification plus fine et à une généralisation accrue des modèles.

---

### Interprétation des résultats

#### Analyse des erreurs du modèle

Les premiers résultats avec VGG16 ont montré une **bonne précision globale**, mais des difficultés persistantes sur certaines classes morphologiquement proches. En particulier :

- **Granulocytes immatures** souvent confondus avec d'autres types cellulaires,
- idem pour les **monocytes**.

Avec DenseNet201 et surtout EfficientNetB0, ces erreurs se réduisent, mais elles ne disparaissent pas totalement. Cela met en évidence la nécessité d’**équilibrer davantage le dataset** et de renforcer la robustesse via de la data augmentation ou des approches hiérarchiques.

| Classe               | Precision | Recall | F1-score | Support |
| -------------------- | --------- | ------ | -------- | ------- |
| basophil             | 0.90      | 0.97   | 0.93     | 183     |
| eosinophil           | 0.99      | 0.90   | 0.94     | 467     |
| erythroblast         | 0.94      | 0.94   | 0.94     | 234     |
| immature_granulocyte | 0.88      | 0.87   | 0.88     | 435     |
| lymphocyte           | 0.89      | 0.97   | 0.92     | 183     |
| monocyte             | 0.83      | 0.88   | 0.85     | 214     |
| neutrophil           | 0.94      | 0.95   | 0.94     | 500     |
| platelet             | 1.00      | 0.98   | 0.99     | 353     |
| **accuracy**         |           |        | 0.93     | 2569    |
| **macro avg**        | 0.92      | 0.93   | 0.93     | 2569    |
| **weighted avg**     | 0.93      | 0.93   | 0.93     | 2569    |

**Tableau 2.** Metriques pour le modèle DenseNet201 (8 classes).

#### Impact de l’analyse des erreurs sur l’amélioration des performances

L’étude des matrices de confusion a permis :

- d’identifier les paires de classes les plus confondues,
- de justifier la mise en place d’oversampling ciblé,
- d’orienter l’architecture choisie (DenseNet/EfficientNet plutôt que VGG16).

L’analyse des erreurs est donc une étape essentielle qui a directement guidé les choix méthodologiques et amélioré la performance finale.

![Matrice de confusion DenseNet201](src/streamlit/assets/DenseNet201_confusion_matrix.png)
**Figure 9.** Matrice de confusion pour le modèle DenseNet201 (8 classes).

#### 3.3.3. Techniques d’interprétabilité utilisées (SHAP, LIME, Skater, Grad-CAM…)

Pour valider que le modèle s’appuie bien sur des régions pertinentes biologiquement, nous avons utilisé **Grad-CAM**.

Les cartes de chaleur montrent que le modèle concentrerait son attention sur le **noyau**, la **morphologie du cytoplasme** et la **granularité spécifique**, notamment pour EfficientNetB0.

Ces observations tendraient à renforcer la confiance dans le modèle, en confirmant qu’il apprend bien des caractéristiques **morphologiques clés**, et non du bruit de fond.

![Grad-CAM DendeNet201](src/streamlit/assets/DenseNet201_gradcam.png)
**Figure 10.** Grad-CAM pour le modèle DendeNet201 (8 classes).

#### Facteurs ayant contribué ou non à une amélioration significative des performances

Plusieurs éléments se sont révélés décisifs pour l’amélioration des performances :

- **Data augmentation contrôlée** (rotation, flips, translations, luminosité/contraste) : amélioration notable du rappel des classes minoritaires,
- **Fine-tuning partiel** (DenseNet201, EfficientNetB0) avec **learning rate réduit** : permet de capter des différences subtiles sans sur-apprentissage,
- **Label smoothing** (EfficientNetB0) : réduit la sur-confiance, meilleure calibration des probabilités,
- **AdamW + régularisation L2** : limite le sur-apprentissage, meilleure généralisation.

En revanche :

- L’entraînement "from scratch" n’a pas été envisagé ici,
- L’extension à 13 classes reste difficile sans données supplémentaires, car certaines sous-classes sont trop proches morphologiquement et trop peu représentées.

![Accuracy DenseNet201](src/streamlit/assets/DenseNet201_accuracy.png)
**Figure 11.** Accuracy pour le modèle DenseNet201 (8 classes).
