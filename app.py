import streamlit as st
from model_handler import openai, gemini

st.set_page_config(page_title="Multi-LLM Chatbot")
st.sidebar.title("Choose an LLM Model")
model_choice = st.sidebar.selectbox("LLM Provider", ["OpenAI", "Gemini", "Mistral"])

st.title("💬 Ask Anything")
user_input = st.text_input("Your question")

if user_input:
    if model_choice == "OpenAI":
        response = openai_handler.ask_openai(user_input)
    elif model_choice == "Gemini":
        response = gemini_handler.ask_gemini(user_input)
    else:
        response = mistral_handler.ask_mistral(user_input)
    st.markdown(f"**Answer:** {response}")
