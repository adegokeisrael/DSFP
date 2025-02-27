import streamlit as st
import numpy as np
import pickle

# Load the trained model
with open("salary_model.pkl", "rb") as file:
    model = pickle.load(file)

# Streamlit UI
st.title("Salary Prediction App")
st.write("Enter the years of experience to predict the salary")

# Input field for user
years_experience = st.number_input("Years of Experience", min_value=0.0, format="%.2f")

# Prediction button
if st.button("Predict"):
    user_input = np.array([[years_experience]])
    prediction = model.predict(user_input)
    
    st.write(f"Predicted Salary: ${prediction[0]:,.2f}")
