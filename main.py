import os
import streamlit as st
from constants import openai_key  # Your Gemini API key variable
from langchain_google_genai import ChatGoogleGenerativeAI

# Set API key for Gemini
os.environ["GOOGLE_API_KEY"] = openai_key

# Streamlit UI
st.title("LangChain Demo with Google Gemini API")
input_text = st.text_input("Search the topic you want:")

# Initialize Gemini model
llm = ChatGoogleGenerativeAI(model="gemini-pro", temperature=0.8)

if input_text:
    response = llm.invoke(input_text)
    st.write(response.content)

    

