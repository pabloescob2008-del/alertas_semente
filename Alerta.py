import requests
import os

TOKEN = os.getenv("8757944104:AAGDGKY3TlDy_hc2sR-na1e1LTEEoIIiq-w")
CHAT_ID = os.getenv("8705265153")

def enviar_alerta(msg):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    requests.post(url, data={
        "chat_id": CHAT_ID,
        "text": msg
    })

enviar_alerta("🚀 Teste rodando no GitHub Actions!")
