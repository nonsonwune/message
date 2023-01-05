from django.conf import settings
import requests
from .models import *

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
        #check user doesnt exist
        if User.objects.filter(username=phoneId).exists():
            user = User.objects.get(username=phoneId)
            user_profile = user.profile
        
        else:
        #Create user
            user = User.objects.create_user(
            username=phoneId,
            email='tester@test.com',
            password='password',
            first_name=profileName)

            #create profile
            user_profile = Profile.objects.create(
            user = user,
            phoneNumber = fromId,
            phoneId = phoneId)

        #create chatSssion
        chat = ChatSession.objects.create(profile = user_profile)
        # send a message
        message = "Welcome to nonso.ai businessplan generator 😃😎 \nI'm going to take you through the process of creating your businessplan right here on whatsapp.\nTo get started, enter your Business Name"
        sendWhatsAppMessage(fromId, message)


#Consinue with function
    if chat.business_name:
        #Test for the number
        try:
            type = int(text.replace(' ', ''))
            if type == 1:
                chat.business_type = 'Private Limited Company (LTD)'
                chat.save()
            elif type == 2:
                chat.business_type = 'Public Limited Company (PLC)'
                chat.save()
            elif type == 3:
                chat.business_type = 'Non-Profit, NGO'
                chat.save()
            elif type == 4:
                chat.business_type = 'Partnership'
                chat.save()
            else:
                message = "Great, Please select the type of business; enter the number corresponding to the business type: \n 1. Private Limited Company (LTD) \n 2. Public Limited Company (PLC) \n 3. Non-Profit, NGO \n 4. Partnership \n\n enter just the number"
                sendWhatsAppMessage(fromId, message)
        except:
            message = 'PLease try again! \nselect the type of business; enter the number corresponding to the business type: \n 1. Private Limited Company (LTD) \n 2. Public Limited Company (PLC) \n 3. Non-Profit, NGO \n 4. Partnership \n\n enter just the number'
    else:
        chat.business_name = text
        chat.save()

        #send the next message
        message = "Great, Please select the type of business; enter the number corresponding to the business type: \n 1. Private Limited Company (LTD) \n 2. Public Limited Company (PLC) \n 3. Non-Profit, NGO \n 4. Partnership \n\n enter just the number"
        sendWhatsAppMessage(fromId, message)



    OPTIONS=1    
    business_name = models.TextField(null=True, blank=True)
    business_type = models.CharField(choices=OPTIONS, null=True, blank=True, max_length=200)
    country = models.TextField(null=True, blank=True)
    prod_serv = models.TextField(null=True, blank=True)
    short_description = models.TextField(null=True, blank=True)
    years = models.IntegerField(null=True, blank=True)
    progress = models.TextField(null=True, blank=True)