import requests
import os

WAHA_BASE_URL = "http://localhost:3000"

def send_message(chat_id: str, text: str):
    url = f"{WAHA_BASE_URL}/api/sendText"
    payload = {
        "chatId": chat_id,
        "text": text,
        "session": "default"
    }
    headers = {"Content-Type": "application/json"}
    
    try:
        response = requests.post(url, json=payload, headers=headers)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print(f"Erro ao enviar mensagem: {e}")
        return None