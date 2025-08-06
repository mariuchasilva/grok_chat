import os
from groq import Groq

client = Groq(
    api_key=os.environ.get('GROQ_API_KEY')
)

pergunta = input("Digite a sua pergunta\n")

chat = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": pergunta
        }
    ],
    model="llama-3.3-70b-versatile"
)
print(chat.choices[0].message.content)