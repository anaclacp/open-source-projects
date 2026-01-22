from fastapi import FastAPI, Request
import uvicorn
from src.waha_client import send_message
from src.rag_engine import get_ai_response

app = FastAPI()

@app.post("/webhook")
async def receive_message(request: Request):
    data = await request.json()
    
    if "payload" in data and "body" in data["payload"]:
        user_msg = data["payload"]["body"]
        sender = data["payload"]["from"]
        
        # Ignora mensagens do próprio bot
        if data["payload"].get("fromMe"):
            return {"status": "ignored"}

        print(f"Mensagem de {sender}: {user_msg}")
        
        # 1. Processa com IA
        resposta_ia = get_ai_response(user_msg)
        
        # 2. Envia de volta
        send_message(sender, resposta_ia)
        
    return {"status": "processed"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)