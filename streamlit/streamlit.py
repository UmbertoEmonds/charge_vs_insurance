import streamlit as st
import pandas as pd
import joblib


st.title("Assurance charges prediction")
st.header("Please provide the following information:")
sex = st.radio("Pick your gender:", ["male", "female"])
smoker = st.radio("Do you smoke?", ["yes", "no"])
height = st.slider("What is your height? (in cm)", 140, 210)
weight = st.slider("What is your weight? (in kg)", 40, 250)
age = st.slider("How old are you?", 18, 100)
children = st.number_input("How many children do you have?", 0, 10)
region = st.selectbox("Where do you live?", ["northwest", "northeast", "southeast", "southwest"])

bmi = round(weight / ((height / 100) ** 2), 2)


new_data = pd.DataFrame({
    "age": [age],
    "children": [children],
    "smoker": [smoker],
    "bmi": [bmi],
    "sex": [sex],
    "region": [region]
})


def add_features(X):
    X = X.copy()
    X["smoker"] = X["smoker"].map({"yes": 1, "no": 0})
    X["smoker_obese"] = X["smoker"] * (X["bmi"] >= 30).astype(int)
    X["age"] = X["age"] ** 2
    return X


if st.button("Predict charges"):
    loaded_model = joblib.load(open("models/insurance_model.pkl", "rb"))
    prediction = loaded_model.predict(new_data)[0]
    st.header(f"You will pay {prediction:.2f} $ charges.")


