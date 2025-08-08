import os
from groq import Groq

def interacao_chat():
    client = Groq(
        api_key=os.environ.get('GROQ_API_KEY')
    )

    conversation = [
        {
            "role": "system",
            "content": "me deseje boas vindas com uma mensagem super curta"
        }
    ]

    while True:
        pergunta = input("Digite a sua pergunta (digite 'sair' para encerrar)\n")
        if pergunta == 'sair':
            print('encerrando...\n\n')
            break
    
        conversation.append(
            {
                "role": "user",
                "content": pergunta
            }
        )

        chat = client.chat.completions.create(
            messages=conversation,
            model="llama-3.3-70b-versatile"
        )
        ai_response = chat.choices[0].message.content

        conversation.append(
            {
                "role": "assistent",
            "content": ai_response  
            }
        )

        print(ai_response)

if __name__ == "__main__":
    interacao_chat()