# 🩺 Assurance Prédiction : Semaine 1 - Analyse Exploratoire (EDA)

## 📌 Présentation du Projet

Dans le cadre de ce projet "Dev Data IA", nous accompagnons un assureur pour mieux comprendre les facteurs influençant les charges médicales. Cette première semaine est dédiée à l'**Exploration des Données (EDA)** afin d'identifier les variables clés et de valider nos hypothèses métier avant la modélisation.

## 🎯 Objectifs

* **Audit de qualité :** Identifier les valeurs manquantes, les doublons et vérifier le typage des données.
* **Analyse Univariée :** Comprendre la distribution de chaque variable (Âge, IMC, Charges, etc.).
* **Analyse Bivariée :** Étudier l'impact des variables (ex: fumeur, région) sur le montant des charges.
* **Étude de Corrélation :** Calculer les coefficients de Pearson/Spearman pour quantifier les relations linéaires.
* **Génération d'Insights :** Extraire 5 à 10 conclusions actionnables pour le métier.
* **Objectif final** : concevoir un modèle IA à régression linéaire pour prédire les charges d'assurance, en se basant sur des données démographiques et médicales

## 📂 Structure du Dépôt (S1)

```text
├── data/
│   └── insurance.csv          # Dataset original (Kaggle)
├── notebooks/
│   └── S1_Exploration.ipynb   # Analyse détaillée et graphiques
├── reports/
│   └── S1_Presentation.pdf    # Slides de synthèse (Fin de semaine)
├── requirements.txt           # Bibliothèques nécessaires
└── README.md

```

## 🛠️ Installation et Configuration

Pour reproduire les analyses de ce notebook :

1. **Cloner le repo :**
```bash
git clone https://github.com/UmbertoEmonds/charge_vs_insurance
```


2. **Installer les dépendances :**
```bash
pip install -r requirements.txt
```


3. **Lancer le Notebook :**
```bash
jupyter notebook notebooks/S1_Exploration.ipynb

```



## 📊 Aperçu des Premiers Constats (Extraits)

* **Distribution des charges :** La variable cible présente une forte asymétrie à droite (quelques individus ont des charges très élevées).
* **Facteur tabac :** Les fumeurs présentent une médiane de charges nettement supérieure aux non-fumeurs.
* **Corrélation IMC/Charges :** Une tendance se dessine, particulièrement forte chez les individus avec un IMC > 30.
* **Corrélation linéaire âge-charges** indépendante des autres paramètres

## 🧪 Hypothèses pour la Semaine 2

Basé sur cette EDA, nous prévoyons pour la phase de modélisation :

1. **Transformation Log :** Appliquer `np.log(charges)` pour normaliser la cible.
2. **Feature Engineering :** Créer une variable binaire `is_obese` (IMC > 30).
3. **Encodage :** Utiliser le *One-Hot Encoding* pour les variables `smoker` et `sex`.

## 👥 L'Équipe

* **Flora**
* **Fatima**
* **Umberto**

---