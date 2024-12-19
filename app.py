import streamlit as st
import pandas as pd
import pickle
import subprocess

subprocess.run(["pip", "install", "numpy"])

# Load the pre-trained model
def load_model():
    with open('best_model.pkl', 'rb') as model_file:
        model = pickle.load(model_file)
    return model
# Title of the app
st.title("Biochar Yield Predictio App")

variable_1 = st.number_input("Fixed Carbon:", value=0)
variable_2 = st.number_input("Volatile matter:", value=0)
variable_3 = st.number_input("Ash:", value=0)
variable_4 = st.number_input("C:", value=0)
variable_5 = st.number_input("H:", value=0)
variable_6 = st.number_input("O:", value=0)
variable_7 = st.number_input("N:", value=0)
variable_8 = st.number_input("Residence time (min):", value=0)
variable_9 = st.number_input("Temperature (°C):", value=0)
variable_10 = st.number_input("Heating rate (°C/min)", value=0)
variable_11 = st.sidebar.selectbox("Type of Feedstock", ['Corncob', 'Corn stover', 'Bagasse', 'Cocopeat', 'Coconut shell', 'Coconut fiber', 'Wheat straw', 'Rice husk', 'Rice Straw', 'Pine', 'Pinewood sawdust ', 'Pine wood', 'Bamboo ', 'Orange Bagasse', 'Rapeseed oil cake', 'Rape stalk ', 'Cassava stem', 'Cassava rhizome', 'Cotton stalk', 'Palm kernel shell', 'Wood stem', 'Wood bark', 'Agro-food waste ', 'Canola hull', 'Oat hull', 'Straw pallet ', 'Vine pruning', 'Poultry litter', 'hinoki cypress'])

# Encoding the inputs
input_data = pd.DataFrame({
    'Fixed Carbon': [variable_1],
    'Volatile matter': [variable_2],
    'Ash': [variable_3],
    'C': [variable_4],
    'H': [variable_5],
    'O': [variable_6],
    'N': [variable_7],
    'Residence time (min)': [variable_8],
    'Temperature (°C)': [variable_9],
    '"Heating rate (°C/min)': [variable_10],
    'Type of Feedstock': [variable_11]

})

# One-hot encode the input data (ensure it matches the training data)
input_encoded = pd.get_dummies(input_data)

# Align columns with the training data (required columns)
model = load_model()
required_columns = model.feature_names_in_  # Get the feature columns from the model
for col in required_columns:
    if col not in input_encoded.columns:
        input_encoded[col] = 0
input_encoded = input_encoded[required_columns]

# Make the prediction
prediction = model.predict(input_encoded)[0]

# Display the prediction
st.subheader(f"The predicted Biochar Yield (%) is: {prediction}")
