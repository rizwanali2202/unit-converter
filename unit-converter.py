import streamlit as st
import pandas as pd
from io import BytesIO


st.title ("Unit Converter App")
st.markdown("### Converts Length, Weight, and Time Instantly")
st.write("Welcome! Select a category, enter a value, and get the converted results.")

# Category selection
category = st.selectbox("Choose a category", ["Length", "Weight", "Time"])

# Unit selection based on category
if category == "Length":
    unit = st.selectbox("Select conversion", ["Kilometers to miles", "Miles to kilometers"])
elif category == "Weight":
    unit = st.selectbox("Select conversion", ["Kilograms to pounds", "Pounds to kilograms"])
elif category == "Time":
    unit = st.selectbox("Select conversion", 
                        ["Seconds to minutes", "Minutes to seconds", "Hours to minutes", 
                         "Minutes to hours", "Hours to days", "Days to hours"])

# User input for value
value = st.number_input("Enter the value to convert", min_value=0.0, format="%.2f")

# Function to perform unit conversions
def convert_units(category, value, unit):
    if category == "Length":
        if unit == "Kilometers to miles":
            return value * 0.621371
        elif unit == "Miles to kilometers":
            return value / 0.621371

    elif category == "Weight":
        if unit == "Kilograms to pounds":
            return value * 2.20462
        elif unit == "Pounds to kilograms":
            return value / 2.20462

    elif category == "Time":
        if unit == "Seconds to minutes":
            return value / 60
        elif unit == "Minutes to seconds":  
            return value * 60
        elif unit == "Hours to minutes":
            return value * 60
        elif unit == "Minutes to hours":
            return value / 60
        elif unit == "Hours to days":
            return value / 24
        elif unit == "Days to hours":  
            return value * 24

    return None  # Return None for invalid selections

# Convert button logic
if st.button("Convert"):
    result = convert_units(category, value, unit)
    if result is not None:
        st.success(f"The result is: {result:.2f}")
    else:
        st.error("Invalid conversion selection. Please try again.")





