from openai import OpenAI

client = OpenAI(base_url="http://localhost:1234/v1", api_key="not-needed")

completion = client.chat.completions.create(
    model="google/gemma-3-4b",
    messages=[
        {"role": "system", "content": "Alway answer in rhymes."},
        {"role": "user", "content": "Introduce yourself."}
    ],
    temperature=0.7
)

print(completion.choices[0].message)