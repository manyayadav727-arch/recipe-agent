from langchain_core.prompts import PromptTemplate
from langchain_groq import ChatGroq

from dotenv import load_dotenv
load_dotenv()
import os
groq_api_key = os.getenv("GROQ_API_KEY") or st.secrets.get("GROQ_API_KEY")

llm = ChatGroq(
    model="llama-3.1-8b-instant",
    api_key=groq_api_key
)

prompt = PromptTemplate(
    input_variables=["ingredients", "cuisine", "diet", "time"],
    template="""
Create a recipe using:
Ingredients: {ingredients}
Cuisine: {cuisine}
Diet: {diet}
Time: {time}

Give step-by-step instructions.
"""
)

chain = prompt | llm

def get_recipe(ingredients, cuisine, diet, time):
    response = chain.invoke({
        "ingredients": ingredients,
        "cuisine": cuisine,
        "diet": diet,
        "time": time
    })
    return response.content