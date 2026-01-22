# ZapBrain - WhatsApp RAG Assistant

Projeto de estudo demonstrando a criação de um chatbot para WhatsApp utilizando IA Generativa (RAG).

Inspiração: 
https://pickle-reading-bd9.notion.site/py_live-020-1169956f3dc980ffa2f5d66dea28a42b
https://pickle-reading-bd9.notion.site/py_live-021-11e9956f3dc9808bb0addcdd86d5da20

## Stack Tecnológica
- **Python 3.10+**
- **FastAPI**: Servidor de Webhook
- **Waha (WhatsApp HTTP API)**: Interface com o WhatsApp
- **LangChain**: Orquestração de IA
- **Docker**: Containerização

## Como rodar
1. Clone o repositório.
2. Crie um arquivo `.env` com sua `OPENAI_API_KEY`.
3. Suba o Waha: `docker-compose up -d`
4. Instale dependências: `pip install -r requirements.txt`
5. Rode o servidor: `python src/main.py`
6. Escaneie o QR Code no painel do Waha (http://localhost:3000)

## Créditos
Baseado nos estudos da py_live do PyCodeBR.