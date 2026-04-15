from langchain.prompts import PromptTemplate

recipe_prompt = PromptTemplate(
    input_variables=["ingredients", "cuisine", "diet", "time"],
    template="""
You are a professional chef AI.

Create a recipe based on:
Ingredients: {ingredients}
Cuisine: {cuisine}
Diet: {diet}
Cooking Time: {time}

Return in this format:

Recipe Name:
Description:
Ingredients:
- item 1
- item 2

Instructions:
1. Step one
2. Step two

Cooking Time:
Tips:
"""
)