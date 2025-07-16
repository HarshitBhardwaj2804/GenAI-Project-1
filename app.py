## Creating a END-TO-END Project
import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
import os
from dotenv import load_dotenv
load_dotenv()

groq_api_key = os.getenv("GROQ_API_KEY")
model = ChatGroq(model = "gemma2-9b-it", groq_api_key = groq_api_key)

instruction = "Translate the following message into {input_instruction}"
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", instruction),
        ("user", "{input_text}")
    ]
)

parser = StrOutputParser()

chain = prompt|model|parser

st.title("Welcome to the language translator using Goggle Gemma2-9b-it LLM Model.")
input_text = st.text_input("Input text here!")
input_instruction = st.text_input("Specify the languange in which you want to translate the text.")

if input_text and input_instruction:
    response = chain.invoke({"input_text": input_text, "input_instruction": input_instruction})
    st.text_area("Translated Message", value = response, height = 100)