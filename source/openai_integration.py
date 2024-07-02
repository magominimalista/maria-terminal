import os
import openai

# Configura a chave de API da OpenAI usando a variável de ambiente 'OPENAI_API_KEY'
openai.api_key = os.getenv('OPENAI_API_KEY')

def generate_openai_response(transcription):
    # Envia uma requisição à API do ChatCompletion usando o modelo GPT-4
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[ { "role": "user", "content": "Responda em poucas palavras: " + transcription } ]
    )

    # Obtém a resposta gerada pelo ChatGPT
    chatgpt_response = response.choices[0].message['content']
    return chatgpt_response
