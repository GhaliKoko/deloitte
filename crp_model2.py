import streamlit as st
import pandas as pd
import numpy as np
import pickle
from xgboost import XGBRegressor


# Charger le modèle
pickle_in = open('final_model.pkl', 'rb')
model = pickle.load(pickle_in)


def predict_price(age, vehicleType_kleinwagen, powerPS, fuelType_diesel, kilometer, fuelType_benzin, brand_bmw,
                  vehicleType_cabrio, notRepairedDamage_new, brand_audi):
    input = np.array([[age, vehicleType_kleinwagen, powerPS, fuelType_diesel, kilometer, fuelType_benzin, brand_bmw,
                       vehicleType_cabrio, notRepairedDamage_new, brand_audi]]).astype(np.float64)
    prediction = model.predict(input)
    return float(prediction)


def main():
    st.title("Predictive Model for Used Car Prices")
    html_temp = """
    <div style="background-color:teal ;padding:10px">
    <h2 style="color:white;text-align:center;">Streamlit Car Price Predictor ML App </h2>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)

    age = st.slider("Age of the Car", 0, 20, 10)
    vehicleType_kleinwagen = st.slider("Vehicle Type Kleinwagen (0 or 1)", 0, 1, 0)
    powerPS = st.slider("Power PS", 0, 200, 100)
    fuelType_diesel = st.slider("Fuel Type Diesel (0 or 1)", 0, 1, 0)
    kilometer = st.slider("Kilometer Driven", 0, 150000, 50000)
    fuelType_benzin = st.slider("Fuel Type Benzin (0 or 1)", 0, 1, 0)
    brand_bmw = st.slider("Is Brand BMW (0 or 1)", 0, 1, 0)
    vehicleType_cabrio = st.slider("Vehicle Type Cabrio (0 or 1)", 0, 1, 0)
    notRepairedDamage_new = st.slider("Is Not Repaired Damage New (0 or 1)", 0, 1, 0)
    brand_audi = st.slider("Is Brand Audi (0 or 1)", 0, 1, 0)

    result = ""
    if st.button("Predict"):
        result = predict_price(age, vehicleType_kleinwagen, powerPS, fuelType_diesel, kilometer, fuelType_benzin,
                               brand_bmw, vehicleType_cabrio, notRepairedDamage_new, brand_audi)
    st.success('The predicted price of the car is {}'.format(round(result)))


if __name__ == '__main__':
    main()
