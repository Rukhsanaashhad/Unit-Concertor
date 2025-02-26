import streamlit as st  

def convert_length(value, from_unit, to_unit):  
    length_units = {  
        'meters': 1,   
        'centimeters': 100,  
        'kilometers': 0.001,  
        'inches': 39.3701,  
        'feet': 3.28084  
    }  
    
    value_in_meters = value / length_units[from_unit]  
    return value_in_meters * length_units[to_unit]  

st.title("Unit Converter")  

st.header("Length Converter")  
value = st.number_input("Enter value:", 0.0)  
from_unit = st.selectbox("From unit:", ['meters', 'centimeters', 'kilometers', 'inches', 'feet'])  
to_unit = st.selectbox("To unit:", ['meters', 'centimeters', 'kilometers', 'inches', 'feet'])  

if st.button("Convert"):  
    converted_value = convert_length(value, from_unit, to_unit)  
    st.success(f"{value} {from_unit} is {converted_value} {to_unit}")  