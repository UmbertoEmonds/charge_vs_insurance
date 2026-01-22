# 🩺 Insurance Cost Prediction

## 📌 Project Overview

As part of this "AI Data Development" project, we are assisting an insurer in better understanding the factors influencing medical costs.

We worked on **Data Exploration (EDA)** to identify key variables and validate our business hypotheses, and we carried out our linear regression project to predict insurance costs for new clients.

## 🎯 Objectives

* **Quality Audit:** Identify missing values, duplicates, and verify data typing.

* **Univariate Analysis:** Understand the distribution of each variable (Age, BMI, Costs, etc.).

* **Bivariate Analysis:** Study the impact of variables (e.g., smoker, region) on the cost amount.

* **Correlation Study:** Calculate coefficients (Pearson method) to quantify linear relationships.

* **Generating Insights:** Extract 5 to 10 actionable conclusions for the business.

* **Final Objective:** Design a linear regression AI model to predict insurance costs, based on demographic and medical data.

## 📂 Repository Structure

```text
├── dataset/
│ └── insurance.csv # Original dataset (Kaggle)
├── insurance_eda.ipynb # EDA
├── insurance_linear_regression.ipynb # Machine Learning model
├── requirements.txt # Mandatory libraries
└── readme.md
```

## 🛠️ Installation and Configuration

#### You need the Jupyter notebook IDE extension.

To reproduce the analyses in this notebook:

1. **Clone the repository:**
```
git clone https://github.com/UmbertoEmonds/charge_vs_insurance
```

2. **Install the dependencies:**

```
pip install -r requirements.txt
```

3. **Launch the Notebooks:**
```bash
jupyter notebook insurance_eda.ipynb
jupyter notebook insurance_linear_regression.ipynb
```

4. **Launch MLFlow**
```bash
mlflow ui
```

## ▶️ Make new predictions

#### Launch Streamlit to make predictions using the UI

```bash
streamlit run ./streamlit/streamlit.py
```

## 📊 Initial Observations Overview

* **Distribution of Charges:** The target variable exhibits a strong right skew (a few individuals have very high charges).

* **Smoker Factor:** Smokers have a significantly higher median charge than non-smokers.

* **BMI/Charges:** A trend is emerging, particularly strong in individuals with a BMI > 30.

## 🧪 Modeling

Based on this EDA, we applied the following plan for the modeling phase:

1. **Delete region feature**

2. **Feature Engineering:** Create a binary variable `is_obese` (BMI > 30). Add interactions `smoker * bmi` and `smoker * is_obese`.

3. **Logarithm transformation:** Compare with and without `log(charges)`. We chose not to use it.

4. **Standardisation:** Scaled numerical features `age` and `children` after split to avoid data leak.

## 👥 The Team

* **[Flora](https://github.com/Flora-Trecul)** 
* **[Fatima](https://github.com/FatimaUY)**
* **[Umberto](https://github.com/UmbertoEmonds)**

---