# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from .models import Document, Article, City
from .forms import SendSmsForm
from .models import Article, City, CityManager, TeamMember, Job, LogSendSms
from twilio.rest import Client
import datetime
from django.shortcuts import redirect
from django.conf import settings


def documents(request):

    try:
        cgu = Document.objects.get(name="Mentions Légales")
    except Document.DoesNotExist:
        cgu = None

    try:
        press_kit = Document.objects.get(name="Kit de Presse")
    except Document.DoesNotExist:
        press_kit = None

    try:
        press_release = Document.objects.get(name="Dossier de Presse")
    except Document.DoesNotExist:
        press_release = None

    try:
        press_release_2 = Document.objects.get(name="Communiqué de Presse")
    except Document.DoesNotExist:
        press_release_2 = None

    context = {
        "cgu": cgu,
        "press_kit": press_kit,
        "press_release": press_release,
        "press_release_2": press_release_2,
    }
    return context


def top_articles(request):
    context = {
        "top_articles": Article.objects.filter(top=True)
    }
    return context


#def maps_api(request):

#    context = {
#        "maps_api": settings.GMAPS_API,
#    }
#    return context


def cities(request):
    context = {
        "cities": City.objects.all().order_by("name"),
    }

    return context


def form_cta(request):

    # Your Account Sid and Auth Token from twilio.com/user/account
    account_sid = settings.TWILIO_SID
    auth_token = settings.TWILIO_TOKEN
    client = Client(account_sid, auth_token)
    from_phone = settings.TWILIO_PHONE

    if request.method == 'POST':
        form_cta = SendSmsForm(data=request.POST)

        if form_cta.is_valid():
            phone_cta = form_cta.cleaned_data["phone_cta"]

            message = client.messages.create(
                str("+33" + phone_cta.replace(" ", "").replace(".", "").lstrip("0")),
                body=str("Bonjour, voici votre lien de téléchargement : onelink.to/pleaseapp"),
                from_=from_phone
            )

            print(message.sid, message.date_created.date)

            LogSendSms(
                phone=phone_cta,
                date=datetime.datetime.utcnow(),
            ).save()

    context = {
        "form_cta": SendSmsForm
    }

    return context
