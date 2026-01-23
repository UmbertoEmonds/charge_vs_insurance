# 🩺 Insurance Cost Prediction

## 📌 Project Overview

As part of this "AI Data Development" project, we are assisting an insurer in better understanding the factors influencing medical costs.

We worked on **Data Exploration (EDA)** to identify key variables and validate our business hypotheses, and we carried out our linear regression project to predict insurance costs for new clients.

## 🎯 Objectives

* **Quality Audit:** Identify missing values, duplicates, and verify data typing.

* **Analysis**

  * **Univariate Analysis:** Understand the distribution of each variable (Age, BMI, Costs, etc.).

  * **Bivariate Analysis:** Study the impact of variables (e.g., smoker, region) on the cost amount.

  * **Correlation Study:** Calculate coefficients (Pearson method) to quantify linear relationships.

  * **Generating Insights:** Extract 5 to 10 actionable conclusions for the business.

* **Modelisation**

  * **Final Objective:** Create a linear regression AI model to predict insurance costs, based on demographic and medical data.

  * **Automatised modelisation:** Implement an automatised pipeline to handle data (feature engineering, data scaling) and apply model.

  * **Strong evaluation:** Use cross validation and try different linear regression models to chose the most efficient final model.

  * **Industrialised model:** Save model to easily reuse it for further deployment.

  * **Prediction demo:** Design a Streamlit UI to predict insurance costs for new clients.

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
jupyter notebook insurance_pipeline.ipynb
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

2. **Feature Engineering:** Create a binary variable `is_obese` (BMI > 30). Add interaction `smoker * is_obese`. Convert `age` to squared `age`.

3. **Logarithm transformation:** Compare with and without `log(charges)`. We chose not to use it, since feature engineering already handles the asymetry of `charges` feature.

4. **Standardisation:** Scale numerical features after split to avoid data leak.

5. **LinearRegression model:** Most efficient linear regression model.

## 🚀 What's next ?

1. **Deployment**

2. **Mistakes analysis:** Some costs are highly undervaluated by our model, we need to understand why.

3. **Increase training data:** Very few data currently (1337), more data could highlight other tendencies and improve model performance.

4. **New features analysis:** Other features might explain the remaining mistakes (alcooholism, diseases...), a V2 model could be designed with more features.

## 👥 The Team

* **[Flora](https://github.com/Flora-Trecul)** 
* **[Fatima](https://github.com/FatimaUY)**
* **[Umberto](https://github.com/UmbertoEmonds)**

---