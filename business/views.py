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
            
            return HttpResponse('success', status=200)