from django.conf import settings
import requests
from models import *

from django.contrib.auth.models import User


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

    
def handleWhatsAppChat(fromId, profileName, phoneId, text):
    #check if existing chat session
    try:
        chat = ChatSession.objects.get(profile__phoneNumber=fromId)
    except:
        #Create user
        user = User.objects.create_user(
            username=profileName,
            email='tester@test.com',
            password='password',
            first_name=profileName,)

        #create profile
        profiles = Profile.objects.create(
            user_profile = user,
            phoneNumber = fromId,
            phoneId = phoneId)

        #create chatSssion
        chat = ChatSession.objects.create(profile = user_profile)