from django.shortcuts import render

from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponse

from .functions import *

import json

# Create your views here.
def home(request):
    return render(request, 'business/index.html', {})


@csrf_exempt
def whatsAppWebhook(request):
    if request.method == 'GET':
        VERIFY_TOKEN = 'ba1eba9c-a425-4ab1-97a6-c7b7e61ffcca'
        mode = request.GET['hub.mode']
        token = request.GET['hub.verify_token']
        challenge = request.GET['hub.challenge']

        if mode == 'subscribe' and token == VERIFY_TOKEN:
            return HttpResponse(challenge, status=200)
        else:
            return HttpResponse('error', status=403)

    if request.method == 'POST':
        data = json.loads(request.body)
        if 'object' in data and 'entry' in data:
            if data['object'] == 'whatsapp_business_account':
                try:
                    for entry in data['entry']:
                        phoneNumber = entry['changes'][0]['value']['metadata']['display_phone_number']
                        phoneId = entry['chamges'][0]['value']['metadata']['phone_number_id']
                        profileName = entry['chamges'][0]['value']['contacts'][0]['profile']['name']
                        whatsAppId = entry['chamges'][0]['value']['contacts'][0][wa_id]
                        fromId = entry['chamges'][0]['value']['messages'][0]['from']
                        messageId = entry['chamges'][0]['value']['messages'][0]['id']
                        timestamp = entry['chamges'][0]['value']['messages'][0]['timestamp']
                        text = entry['chamges'][0]['value']['messages'][0]['text']['body']

                        phoneNumber = '2348136514087'
                        message = 'RE: {} was received'.format(text)
                        sendWhatsAppMessage(phoneNumber, message)
                except:
                    pass
        return HttpResponse('success', status=200)