import google.generativeai as genai

# Paste your API key directly here (ONLY for testing)
GEMINI_API_KEY = "AIzaSyD3f5eX8WXB1EuFA2ylOB4ooVW3Qb_mW5A"

genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel(model_name="gemini-pro")

def ask_gemini(prompt):
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Gemini Error: {e}"
