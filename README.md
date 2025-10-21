# Blood cells classification

L’objectif de ce projet est d’identifier les différents types de cellules du sang à l’aide d'algorithmes de computer vision. La densité et l’abondance relative des cellules du sang dans le frottis est cruciale pour le diagnostic de nombreuses pathologies, comme par exemple pour la leucémie qui repose sur le ratio de lymphocytes. L’identification de leucocytes anormaux dans des pathologies telles que la leucémie pourrait compléter cette première partie.
Développer un outil capable d'analyser les cellules à partir de frottis sanguins pourrait faciliter le diagnostic de certaines pathologies mais aussi être utilisé à but de recherche.

## Rapports

1. Rapport 1: `reports/rendu1_dataviz_preprocessing.pdf`

## Notebooks

1. Data Visualization (Data Viz'): `notebooks/nb_1_1_dataviz.ipynb`
2. Exploratory Data Analysis (EDA): `notebooks/nb_1_2_eda.ipynb`
3. Nettoyage des données: `notebooks/nb_2_1_cleaning.ipynb`
4. Réduction des biais: `notebooks/nb_2_2_bias.ipynb`
5. Traitement: `notebooks/nb_2_3_preprocessing.ipynb`

---

## Environnement virtuel (venv) avec Python 3.11.12

_Installation de Python 3.11.12_
Assurez-vous que Python 3.11.12 est installé sur votre machine. Cette version est nécessaire afin d'assurer la compatibilité avec TensorFlow. Vous pouvez vérifier la version en ouvrant un terminal et en exécutant :
\$ python --version
ou
\$ python3 --version

Si tel n'est pas le cas, [téléchargez et installez Python](https://www.python.org/downloads/) depuis la page officielle.

_Création de l’environnement virtuel_
Dans le répertoire racine du projet, créez un environnement virtuel en lançant la commande suivante :
\$ python -m venv venv
ou
\$ python3 -m venv venv

Si vous utilisez un [IDE comme VSCode](https://code.visualstudio.com/docs/python/environments), renseignez-vous auprès de la documentation officielle pour créer un environement virtuel.

---

## Installation des dépendances

\$ `pip install -r requirements.txt`

---

## Téléchargement du jeu de données

\$ `git clone https://github.com/DataScientest-Studio/dec24_cds_blood_cells.git` # Voir https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository#cloning-a-repository

Télécharger le dataset https://data.mendeley.com/datasets/snkd93bnjr/1 et copier les dossiers (`basophil`, `eosinophil`, `erythroblast`, `ig`, `lymphocyte`, `monocyte`, `neutrophil`, `platelet`) dans `data/raw/`

---

## Organisation du projet

    ├── LICENSE
    ├── README.md          <- The top-level README for developers using this project.
    ├── data               <- Should be in your computer but not on Github (only in .gitignore)
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   ├── interim        <- The ongoing dataset.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's name, and a short `-` delimited description, e.g.
    │                         `1.0-alban-data-exploration`.
    │
    ├── references         <- Data dictionaries, manuals, links, and all other explanatory materials.
    │
    ├── reports            <- The reports that you'll make during this project as PDF
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── features       <- Scripts to turn raw data into features for modeling
    │   │   └── build_features.py
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │   │                 predictions
    │   │   ├── predict_model.py
    │   │   └── train_model.py
    │   │
    │   ├── visualization  <- Scripts to create exploratory and results oriented visualizations
    │   │   └── visualize.py

---
