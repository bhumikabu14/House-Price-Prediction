import pandas as pd
import pickle 
import streamlit as st

model = pickle.load(open('House_prediction_model.pkl','rb'))

st.header('House Prices Prediction')
data = pd.read_csv('Cleaned_data.csv')

loc = st.selectbox('Choose the location', data['location'].unique())
sqft = st.number_input('Enter Total sqft')
beds = st.number_input('Enter No of Bedrooms')
bath = st.number_input('Enter No of Bathrooms')
balc = st.number_input('Enter No of Balconies')


input = pd.DataFrame([[loc,sqft,bath,balc,beds]],columns=['location','total_sqft','bath','balcony','bedrooms'])

if st.button("Predict Price"):
    output = model.predict(input)
    out_str = f"Price of the House is ₹ {output[0]*100000:,.2f}"
    st.success(out_str)