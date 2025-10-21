### Contexte

L’**hématopoïèse** est le processus par lequel la moelle osseuse produit l’ensemble des cellules sanguines. Ce mécanisme débute à partir des cellules souches hématopoïétiques (HSC), qui se différencient en cellules progénitrices capables de suivre deux grandes voies : la lignée myéloïde et la lignée lymphoïde.

Dans la lignée myéloïde, on trouve la production des granulocytes, incluant les **neutrophiles**, les **éosinophiles** et les **basophiles**, qui jouent un rôle essentiel dans la défense contre les infections. Avant leur maturité, ces **granulocytes** passent par plusieurs stades immatures (promyelocytes, myélocytes et métamyélocytes) qui reflètent leur processus de différenciation progressive. Parallèlement, les **monocytes**, également issus de cette voie, se transforment en macrophages ou en cellules dendritiques, participant à la phagocytose et à la régulation de la réponse immunitaire. Les **érythroblastes**, quant à eux, sont les précurseurs des érythrocytes, chargés du transport de l’oxygène, tandis que les mégacaryocytes se développent pour produire les **plaquettes** (ou thrombocytes), indispensables à la coagulation.

Du côté de la lignée lymphoïde, les cellules se spécialisent en **lymphocytes** (B, T et NK), essentiels pour les fonctions spécifiques de l’immunité adaptative et innée.

![Hématopoïèse](src/streamlit/assets/Hematopoiese_simple.png)
**Figure 1.** L'hématopoïèse (source [Wikipedia](https://fr.wikipedia.org/wiki/Hématopoïèse)).

Ainsi, l’hématopoïèse est un processus ordonné et dynamique qui génère un ensemble diversifié de cellules, chacune ayant une fonction précise dans la défense et le maintien de l’homéostasie de l’organisme. Ce processus est particulièrement exploité dans les datasets d’imagerie, où l’analyse et la classification de ces cellules permettent d’apporter des éclairages précieux pour le diagnostic et la recherche médicale.

---

### Objectif

L’objectif de ce projet est d’identifier les différents types de cellules du sang à l’aide d’algorithmes de computer vision et deep learning.

L’analyse des frottis sanguins repose traditionnellement sur l’expertise humaine, qui peut varier d’un laborantin à l’autre. Le recours aux techniques de deep learning permet i) de **standardiser l’analyse** et ainsi réduire la variabilité entre les observateurs, et ii) d'**accélérer le diagnostic** grâce à un outil (modèle) de dépistage rapide et fiable.

Le modèle développé pourrait s'ouvrir dans un deuxième temps à l'identification de cellules sanguines cancéreuses, et donc permettre le diagnostic de pathologies telles que la leucémie, où le ratio de lymphocytes joue un rôle crucial.

---

### Cadre

#### Sources de données

###### Datasets de base

Acevedo, A., Merino A., Alférez S. et al. A dataset of microscopic peripheral blood cell images for development of automatic recognition systems. Data in Brief, 30 (2020). [https://doi.org/10.1016/j.dib.2020.105474](https://doi.org/10.1016/j.dib.2020.105474)

- **Mendeley Data** : [Dataset initial](https://data.mendeley.com/datasets/snkd93bnjr/1)
- **Kaggle** : [Blood Cells Image Dataset](https://www.kaggle.com/datasets/unclesamulus/blood-cells-image-dataset/data)

###### Datasets complémentaires potentiels

Kouzehkanan, Z.M., Saghari, S., Tavakoli, S. et al. A large dataset of white blood cells containing cell locations and types, along with segmented nuclei and cytoplasm. Sci Rep 12, 1123 (2022). [https://doi.org/10.1038/s41598-021-04426-x](https://doi.org/10.1038/s41598-021-04426-x)

Park, S., Cho, H., Woo, B.M. et al. A large multi-focus dataset for white blood cell classification. Sci Data 11, 1106 (2024). [https://doi.org/10.1038/s41597-024-03938-1](https://doi.org/10.1038/s41597-024-03938-1)

#### 0utils d’intelligence artificielle

##### Méthodes et techniques

**Deep Learning et CNNs**
Les réseaux de neurones convolutifs (CNN) seront au cœur de l’analyse, permettant d’extraire des caractéristiques pertinentes à partir des images.

##### Outils et bibliothèques

- **Bibliothèques de dataViz'** : Matplotlib, Seaborn et Plotly pour l’exploration et la visualisation des données.
- **Frameworks** : TensorFlow et Keras ou PyTorch pour le développement et l’entraînement des modèles.

#### Défis et risques

L'analyse d'images médicales par des techniques de computer vision et deep learning peut se révéler complexe et chronophage. Par ailleurs, avec des datasets limités ou déséquilibrés, le risque d’overfitting est plausible, ce que nous devrons prendre en compte. Enfin, l’entraînement de modèles deep learning requiert d’importantes ressources matérielles (GPU, mémoire), ce qui peut imposer des contraintes en termes de temps et de budget.
