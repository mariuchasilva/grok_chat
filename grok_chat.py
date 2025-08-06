import os
from groq import Groq

client = Groq(
    api_key=os.environ.get('GROQ_API_KEY')
)

chat = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "Explique a importância de modelos de linguagens rapidos"
        }
    ],
    model="llama-3.3-70b-versatile"
)
print(chat.choices[0].message.content)