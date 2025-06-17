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
