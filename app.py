import streamlit as st
import pandas as pd
import numpy as np
import pickle
from xgboost import XGBRegressor

# Charger le modèle
with open('best_xgb_model.pkl', 'rb') as f:
    model = pickle.load(f)

# Définir la page
st.title("Moteur de pricing de véhicule d'occasions")


# Définir les sliders pour les caractéristiques numériques dans la barre latérale
age = st.sidebar.slider('Age', min_value=0, max_value=100, value=50)
powerPS = st.sidebar.slider('Power PS', min_value=0, max_value=500, value=100)
kilometer = st.sidebar.slider('Kilometer', min_value=0, max_value=200000, value=100000)

# Définir les selectbox pour les caractéristiques catégoriques dans la barre latérale
st.sidebar.markdown('### Si le véhicule est une kleinwagen, sélectionnez 1')
vehicleType_kleinwagen = st.sidebar.selectbox('Vehicle Type - Kleinwagen', options=[0,1])

st.sidebar.markdown('### Choisissez 1 pour le type de carburant du véhicule')
fuelType_diesel = st.sidebar.selectbox('Diesel', options=[0,1])
fuelType_benzin = st.sidebar.selectbox('Benzin', options=[0,1])

st.sidebar.markdown('### Sélectionnez 1 si le véhicule est une BMW ou une Audi')
brand_bmw = st.sidebar.selectbox('BMW', options=[0,1])
brand_audi = st.sidebar.selectbox('Audi', options=[0,1])

st.sidebar.markdown("### Si le véhicule a subi un dommage qui n'a pas été reparé, sélectionnez 1. Si non, sélectionnez 0. Si vous ne savez pas, sélectionnez 2")
notRepairedDamage_new = st.sidebar.selectbox('', options=[0,1,2])

st.sidebar.markdown('### Si le véhicule est un cabrio, sélectionnez 1')
vehicleType_cabrio = st.sidebar.selectbox('Cabrio', options=[0,1])

# Créer un DataFrame à partir des entrées
data = {'age': [age], 'powerPS': [powerPS], 'kilometer': [kilometer],
        'vehicleType_kleinwagen': [vehicleType_kleinwagen], 'fuelType_diesel': [fuelType_diesel],
        'fuelType_benzin': [fuelType_benzin], 'brand_bmw': [brand_bmw],
        'vehicleType_cabrio': [vehicleType_cabrio], 'notRepairedDamage_new': [notRepairedDamage_new],
        'brand_audi': [brand_audi]}
df = pd.DataFrame(data)

# Faire une prédiction et l'afficher
prediction = model.predict(df)
st.header(f'La valeur du véhicule est de {round(prediction[0])} euros.')
