# # 08 : Streamlit BMI Calculator

import streamlit as st

st.title("BMI CALCULATOR 🏋️‍♀️")

height = st.slider("Enter your height (in cm):", 100, 250, 175)
weight = st.slider("Enter your weight (in kg):", 40, 200, 70)

bmi = weight / ((height / 100) ** 2)

st.subheader(f"Your BMI is {bmi:.2f} 🌟")

st.write("### BMI Categories ###")
st.write("1. Underweight: BMI less than 18.5 🏃‍♀️")
st.write("2. Normal Weight: BMI between 18.5 and 24.9 🍏")
st.write("3. Overweight: BMI between 25 and 29.9 🍔")
st.write("4. Obesity: BMI 30 or greater 🍟")