### Difficultés rencontrées

Au cours du projet, plusieurs contraintes ont ralenti la progression.
Les ressources humaines ont constitué le principal frein : initialement prévu pour quatre étudiants,
le projet a finalement été mené par deux membres, en parallèle d’activités professionnelles et d’un emploi du temps dense.
Les ressources matérielles limitées, notamment l’accès restreint aux GPU, ont également freiné l’expérimentation de modèles plus complexes.
La gestion des versions de jeux de données - originales, normalisées ou augmentées - a nécessité une rigueur importante pour garantir la reproductibilité.
Enfin, comme dans tout travail collaboratif, la coordination des contributions et l’intégration des résultats ont parfois entraîné des doublons ou des décalages.
Malgré ces difficultés, l’équipe a maintenu un rythme régulier et a atteint les principaux objectifs.

---

### Bilan

Le projet a permis de construire un pipeline complet de classification d’images biomédicales,
depuis le nettoyage et le prétraitement des données jusqu’à la modélisation avancée par réseaux de neurones.
Les différentes étapes ont été optimisées pour garantir robustesse et cohérence : équilibrage du dataset,
data augmentation réaliste, exploration de plusieurs architectures CNN et validation par interprétabilité (Grad-CAM).
Les résultats obtenus, avec une précision globale comprise entre 92 et 93 %, démontrent la faisabilité de la classification automatique des cellules sanguines.
L’évolution progressive des modèles, de VGG16 à DenseNet201 puis EfficientNetB0, a montré une amélioration constante des performances et une meilleure généralisation.
Ce travail illustre la démarche scientifique adoptée : établir une baseline fiable, évaluer systématiquement les gains et documenter chaque choix technique.

#### Résultats obtenus et comparaison aux benchmarks

Les modèles classiques comme le SVC ont servi de référence initiale avec une précision d’environ 79 %.
Les modèles de deep learning ont ensuite permis de dépasser cette baseline, atteignant des niveaux de performance comparables à l’état de l’art.
Les résultats se rapprochent des meilleures études publiées, qui rapportent entre 96 et 99 % d’accuracy après un entraînement long.
Bien que légèrement inférieurs, nos scores sont cohérents compte tenu des ressources limitées et du temps d’entraînement réduit.

#### Potentiel d’intégration métier

Le modèle développé, sans prétendre remplacer l’expertise humaine, pourrait être intégré dans un environnement de laboratoire
pour assister les techniciens en pré-annotation des frottis sanguins, réduisant ainsi le temps d’analyse.
Il possède également un fort potentiel pédagogique pour l’enseignement de la morphologie cellulaire.
Avec un enrichissement du dataset par des images pathologiques, ce type de modèle pourrait devenir un outil de dépistage assisté par l’IA,
utile dans le diagnostic précoce de certaines hémopathies comme les leucémies.

---

### Suite du projet

Plusieurs perspectives ont émergé à l’issue de ce travail.
D’abord, l’enrichissement du jeu de données avec de nouvelles sources d’images permettrait de réduire les déséquilibres
et d’améliorer la capacité de généralisation des modèles.
L’exploration de méthodes d’augmentation avancées, comme les GANs, pourrait également contribuer à la création de jeux synthétiques réalistes.
Enfin, l’optimisation d’architectures plus récentes ou spécialisées pour l’imagerie biomédicale constitue une piste prometteuse,
de même que l’utilisation de techniques d’ensemble (ensembling) pour combiner les forces de plusieurs modèles.

#### Vers une classification hiérarchique et multimodale

Une évolution naturelle du projet serait de mettre en place une classification hiérarchique,
dans laquelle un premier modèle identifierait les grandes familles cellulaires
avant de déléguer la spécialisation à des classifieurs dédiés.
Parallèlement, l’arrivée de modèles multimodaux, capables de combiner image et texte,
ouvre la voie à des approches intégrant des annotations ou des données cliniques.

#### Contribution scientifique et perspectives

Au-delà des performances, le projet a contribué à formaliser une méthodologie reproductible pour la classification cellulaire.
Les bonnes pratiques documentées - normalisation, filtrage des outliers, validation par Grad-CAM -
constituent une base utile pour d’autres travaux en vision biomédicale.
Les limites rencontrées, notamment le déséquilibre des classes et la difficulté à distinguer treize sous-types cellulaires,
soulignent la nécessité de jeux de données plus riches et mieux standardisés.
À long terme, ce type de pipeline pourrait s’intégrer à des workflows cliniques pour le dépistage automatisé de maladies hématologiques.
