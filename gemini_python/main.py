import os
from dotenv import load_dotenv
from google import genai
load_dotenv()

gemini_key = os.environ.get('GEMINI_KEY')
gemini_client = genai.Client(api_key=gemini_key)
gemini_model = 'gemini-2.5-flash'
chat = gemini_client.chats.create(model=gemini_model)

while True:
    mensaje: str = input('>')
    if mensaje == 'exit'.lower():
        respuesta = chat.send_message(message='Voy a salir del chat, genera un mensaje de despedida muy corto relacionado a la conversación y sin opciones.')
        print(respuesta.text)
        break
    respuesta = chat.send_message(mensaje)
    print(respuesta.text)