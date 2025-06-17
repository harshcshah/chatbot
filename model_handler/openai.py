import os
from openai import OpenAI

client = OpenAI(api_key="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"

def ask_openai(prompt):
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"OpenAI Error: {e}"
