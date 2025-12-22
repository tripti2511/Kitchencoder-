import pandas as pd
import streamlit as st
from fuzzywuzzy import process  # AI logic for similarity search

# 1. Load the recipe data (Backend)
try:
    df = pd.read_csv("backend/recipes1.csv")
except FileNotFoundError:
    st.error("Dataset not found. Please ensure 'backend/recipes1.csv' exists.")
    st.stop()

# 2. Streamlit UI
st.set_page_config(page_title="Kitchen Coder AI", page_icon="🍇")
st.title("Kitchen coder 🍇 - AI Edition")
st.markdown("### Intelligent Cooking Guidance System")

dish_name = st.text_input("What would you like to cook today? (e.g., 'Piza', 'Chiken')")

if dish_name:
    # --- START OF AI COMPONENT ---
    # Instead of just pandas filtering, we use fuzzy matching to handle typos
    choices = df['Dish Name'].tolist()
    
    # process.extractOne uses Levenshtein Distance to find the closest match
    best_match, score = process.extractOne(dish_name, choices)
    
    # If the AI is at least 70% confident, we show the result
    if score >= 70:
        # Filter the dataframe for our AI's best guess
        matched = df[df['Dish Name'] == best_match]
        recipe_info = matched.iloc[0]
        
        st.success(f"I think you're looking for: **{best_match}** (Confidence: {score}%)")
        
        # 3. Displaying Results
        col1, col2 = st.columns(2)
        with col1:
            st.write(f"**Cuisine:** {recipe_info['Cuisine']}")
        with col2:
            st.write(f"**Cooking Time:** {recipe_info['Cooking Time']} mins")
            
        st.write(f"**Ingredients:** {recipe_info['Ingredients']}")
        st.write(f"**Steps:** {recipe_info['Recipe Steps']}")
        st.info(f"**Pro Tip:** {recipe_info['Tips']}")
    else:
        st.error("Sorry, even my AI couldn't find a close match for that. Try a different dish name!")
    # --- END OF AI COMPONENT ---
