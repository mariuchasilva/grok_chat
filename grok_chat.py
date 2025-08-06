import os
from groq import Groq

def interacao_chat(pergunta):
    client = Groq(
        api_key=os.environ.get('GROQ_API_KEY')
    )

    print("ola")
    chat = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": pergunta
            }
        ],
        model="llama-3.3-70b-versatile"
    )
    return chat.choices[0].message.content

if __name__ == "__main__":
    while True:
        pergunta = input("Digite a sua pergunta (digite 'sair' para encerrar)\n")
        if pergunta == 'sair':
            print('encerrando...\n\n')
            break
        print(interacao_chat(pergunta))