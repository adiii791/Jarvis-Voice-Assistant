from openai import OpenAI

client = OpenAI(api_key="sk-your-valid-key-here")

completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful AI assistant named Jarvis."},
        {"role": "user", "content": "What is coding?"}
    ]
)

print(completion.choices[0].message.content)
