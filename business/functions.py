from django.conf import settings
import requests


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

phoneNumber = "2348136514087"
message = "Hello There, \n This is our first Django WhatsappMessage. \n glad to have you here. \n \n Best Regards. \n Nonso Nwune"
ans = sendWhatsAppMessage(phoneNumber, message)