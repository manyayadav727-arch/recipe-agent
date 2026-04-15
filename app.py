import streamlit as st
from agent import get_recipe

from dotenv import load_dotenv
load_dotenv()
import os
groq_api_key = os.getenv("GROQ_API_KEY") or st.secrets.get("GROQ_API_KEY")

st.set_page_config(page_title="Recipe Generator", layout="centered")

st.title("🍳 AI Recipe Creator")

st.write("Enter your ingredients and preferences")

# Inputs
ingredients = st.text_area("Ingredients (comma separated)")
cuisine = st.selectbox("Cuisine", ["Indian", "Italian", "Chinese", "Mexican"])
diet = st.selectbox("Diet", ["None", "Vegetarian", "Vegan", "Keto"])
time = st.selectbox("Cooking Time", ["15 min", "30 min", "45 min"])

# Button
if st.button("Generate Recipe"):
    if ingredients.strip() == "":
        st.warning("Please enter ingredients")
    else:
        with st.spinner("Cooking up something delicious... 👨‍🍳"):
            recipe = get_recipe(ingredients, cuisine, diet, time)

        st.success("Recipe Ready!")
        st.markdown(recipe)
