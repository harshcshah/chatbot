import os
import google.generativeai as genai

# Load Gemini API key from environment
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Configure Gemini
genai.configure(api_key=GEMINI_API_KEY)

# Create the model (correct syntax)
model = genai.GenerativeModel(model_name="gemini-pro")

def ask_gemini(prompt):
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Gemini Error: {e}"
