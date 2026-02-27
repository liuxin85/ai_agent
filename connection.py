import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv('OPENAI_API_KEY')
base_url = os.getenv("BASE_URL")

if not api_key:
    raise ValueError("No API key found. Please check your .env file.")

client = OpenAI(api_key=api_key, base_url=base_url)

def ask_chatgpt(user_message):
    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[{"role": "system", "content": "Your are a helpful assistent."},
                  {"role": "user", "content": user_message}],
                  temperature=0.7,
    )
    return response.choices[0].message.content

user = "What is the capital of France?"
response = ask_chatgpt(user)
print(response)