## Medical Insurance Cost Prediction
import streamlit as st
import pandas as pd
import pickle

# Load the Model 

with open('Model/insurance_prediction.pkl', 'rb') as file:
    model_file = pickle.load(file)

# Title of Page
st.title('Medical Insurance Cost Prediction')

with st.form("my_form"):
    # Input form
    children = st.number_input('Children', min_value=0, max_value=10)
    smoker = st.selectbox('Smoker', ['yes','no'])
    age = st.number_input('Age', min_value=1, max_value=100)
    bmi = st.number_input('BMI', min_value=0, max_value=55)
    gender = st.selectbox('Gender', ['male', 'female'])
    region = st.selectbox('Region', ['southwest', 'southeast', 'northwest', 'northeast'])

    # Preprocess the input
    new_data = pd.DataFrame({
    'children':children,
    'sex':gender,
    'age':age,
    'bmi':bmi,
    'smoker':smoker,
    'region': region, },index=[0])
    # use dataframe to predict result by passing into predict method
    result = model_file.predict(new_data)[0]
    
   # create a button in the form
    submitted = st.form_submit_button("Predict")
    if submitted:
        st.write("Medical Insurance Cost", result)
