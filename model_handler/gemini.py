from dotenv import load_dotenv
load_dotenv()

import os
import google.generativeai as genai

# Configure with your API key from the .env file
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Use the correct model name: gemini-1.5-pro or gemini-1.0-pro
model = genai.GenerativeModel("gemini-1.5-pro")  # ✅ Correct model name

def ask_gemini(prompt):
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Gemini Error: {e}"
