from django.urls import path
from . import views


urlpatterns = [
path('', views.home, name='home')
path('14b5a3b6-fd24-4132-bac3-d2460256710f', views.whatsAppWebhook, name='whatsapp-webhook')
]

#nonsonwune.ml/14b5a3b6-fd24-4132-bac3-d2460256710f
#Token: ba1eba9c-a425-4ab1-97a6-c7b7e61ffcca