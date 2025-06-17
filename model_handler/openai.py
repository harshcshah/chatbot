from openai import OpenAI

# 🔐 Static API key (for test purposes only)
client = OpenAI(api_key="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")

def ask_openai(prompt):
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"OpenAI Error: {e}"
