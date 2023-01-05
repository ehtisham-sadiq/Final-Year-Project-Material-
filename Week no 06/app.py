import streamlit as st
import pickle
import pandas as pd

# Load the Model 

with open('Model/titanic_Survival.pkl', 'rb') as file:
    model_file = pickle.load(file)

# Title of Page
st.title('Titanic Survival App')

with st.form("my_form"):
    # Input form
    age = st.number_input('Age', min_value=0, max_value=100)
    fare = st.number_input('Fare', min_value=0, max_value=500)
    pclass = st.number_input('Class', min_value=1, max_value=3)
    TravelAlone = st.number_input('TravelAlone', min_value=0, max_value=1)
    gender = st.selectbox('Gender', ['male', 'female'])
    embarked = st.selectbox('Embarked', ['S', 'C', 'Q'])

    # Preprocess the input
    input_dict = {
    'age': [age],
    'fare': [fare],
    'sex': [gender],
    'embarked': [embarked],
    'pclass':[pclass],
    'TravelAlone':[TravelAlone]
    }
    input_df = pd.DataFrame(input_dict, index=[0])
    result = model_file.predict(input_df)[0]
    submitted = st.form_submit_button("Predict")
    if submitted:
        if result == '0':
            st.write('Sorry, you did not survive the Titanic.')
        else:
            st.write('Congratulations, you survived the Titanic!')

