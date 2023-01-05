from django.conf import settings
import requests
from .models import *


def sendWhatsAppMessage(phoneNumber, message):
    headers = {"Authorization": settings.WHATSAPP_TOKEN}
    payload = {
        "messaging_product": "whatsapp",
        "recipient_type": "individual",
        "to": phoneNumber,
        "type": "text",
        "text": {"body": message}
    }

    response = requests.post(settings.WHATSAPP_URL, headers=headers, json=payload)
    ans = response.json()
    return ans

    
def handleWhatsAppChat(fromId, text):
    #check if existing chat session
    try:
        chat = chatSession.objects.get(profile__phoneNumber=fromID)
    except:
        