import pandas as pd
import streamlit as st

# Load CSV
df = pd.read_csv("backend/recipes1.csv")

# Streamlit UI
st.title("Kitchen coder🍇")
dish_name = st.text_input("Enter dish name:")

if dish_name:
    dish_name_lower = dish_name.lower()
    matched = df[df['Dish Name'].str.lower() == dish_name_lower]
    if not matched.empty:
        recipe_info = matched.iloc[0]
        st.write(f"**Dish Name:** {recipe_info['Dish Name']}")
        st.write(f"**Cuisine:** {recipe_info['Cuisine']}")
        st.write(f"**Cooking Time:** {recipe_info['Cooking Time']} mins")
        st.write(f"**Ingredients:** {recipe_info['Ingredients']} ")
        st.write(f"**Tips:** {recipe_info['Tips']}")
        st.write(f"**Recipe Steps:** {recipe_info['Recipe Steps']}")
    else:
        st.write("Sorry, recipe not found.")
