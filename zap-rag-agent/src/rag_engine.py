from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
import os

def get_ai_response(user_message: str):
    contexto = """
    O projeto ZapBrain é um assistente open source criado para estudos.
    Ele usa FastAPI, Docker e Waha para conectar o WhatsApp a LLMs.
    O criador é um desenvolvedor Python Full Stack.
    """
    
    template = """
    Você é um assistente útil. Use o contexto abaixo para responder à pergunta do usuário.
    Se a resposta não estiver no contexto, diga que não sabe.
    
    Contexto: {context}
    
    Pergunta: {question}
    """
    
    prompt = PromptTemplate.from_template(template)
    llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)
    
    chain = prompt | llm
    
    try:
        response = chain.invoke({"context": contexto, "question": user_message})
        return response.content
    except Exception as e:
        return "Desculpe, meu cérebro de IA está offline no momento."