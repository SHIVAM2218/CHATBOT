import os
import streamlit as st
from constants import openai_key  # your Gemini key here
from langchain_google_genai import ChatGoogleGenerativeAI

os.environ["GOOGLE_API_KEY"] = openai_key

st.title("SHIVAM ka apna AIchatbot")

input_text = st.text_input("Enter your prompt:")

# Use correct model for Gemini 2.5
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-pro",  # or "gemini-2.5-flash"
    temperature=0.7
)

if input_text:
    response = llm.invoke(input_text)
    st.write(response.content)

