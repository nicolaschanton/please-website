# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.template import loader
from django.http import HttpResponse
from please_website_app import forms
from django.shortcuts import redirect, render
from django.template.loader import get_template
from django.http import Http404
from .models import Article, City, CityManager, TeamMember, Job, LogLeadForm, Category, CandidateCityManager, \
    LogContactForm, LogContactFormCity, LogContactFormDelivery, LogContactFormMerchant, Merchant, DeliveryMan, Quote
from .send_email import send_email
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
import datetime
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.shortcuts import HttpResponseRedirect
from random import randint
from django.conf import settings
from django.template import RequestContext
from django.core.files.storage import FileSystemStorage


def index(request):

    categories = []
    categories_name = []

    for category in Category.objects.all():
        if category.name not in categories_name:
            categories_name.append(category.name)
            categories.append(Category.objects.filter(name=category.name).first())
        else:
            continue

    context = {
        "top_articles": Article.objects.filter(top=True),
        "categories": categories,
    }

    template = loader.get_template('please_website_app/index.html')
    return HttpResponse(template.render(context, request))


def presse(request):

    context = {
        "articles": Article.objects.all(),
    }
    template = loader.get_template('please_website_app/presse.html')
    return HttpResponse(template.render(context, request))


def team(request):

    context = {
        "team_members": TeamMember.objects.all(),
    }
    template = loader.get_template('please_website_app/team.html')
    return HttpResponse(template.render(context, request))


def jobs(request):

    context = {
        "jobs": Job.objects.filter(),
    }
    template = loader.get_template('please_website_app/jobs.html')
    return HttpResponse(template.render(context, request))


def city_manager(request):

    context = {
    }
    template = loader.get_template('please_website_app/city_manager.html')
    return HttpResponse(template.render(context, request))


def city_manager_franchise(request):

    context = {
    }
    template = loader.get_template('please_website_app/city_manager_franchise.html')
    return HttpResponse(template.render(context, request))


def city_manager_creation_business(request):

    context = {
    }
    template = loader.get_template('please_website_app/city_manager_creation_business.html')
    return HttpResponse(template.render(context, request))


def city_manager_idee_business(request):

    context = {
    }
    template = loader.get_template('please_website_app/city_manager_idee_business.html')
    return HttpResponse(template.render(context, request))


def city_manager_recherche_emploi(request):

    context = {
    }
    template = loader.get_template('please_website_app/city_manager_recherche_emploi.html')
    return HttpResponse(template.render(context, request))


def testimonials(request):

    context = {
        "testimonials": CityManager.objects.all(),
    }

    template = loader.get_template('please_website_app/temoignages.html')
    return HttpResponse(template.render(context, request))


def collectivites(request):

    context = {
    }
    template = loader.get_template('please_website_app/collectivites.html')
    return HttpResponse(template.render(context, request))


def city(request, name):

    try:
        city_asked = City.objects.get(name=name)
        center = (str(city_asked.gps_coordinates_lat).replace(",", "."), str(city_asked.gps_coordinates_long).replace(",", "."))
        categories_asked = Category.objects.filter(city=city_asked)

        try:
            coordinates_raw = city_asked.gps_coordinates.split(" ")

            coordinates = []

            for couple in coordinates_raw:
                lng = str(couple.split(",")[0]).replace(",", ".")
                lat = str(couple.split(",")[1]).replace(",", ".")

                dic = (lat, lng)

                coordinates.append(dic)
        except:
            coordinates = []

    except City.DoesNotExist:
        raise Http404("Cette ville n'existe pas")

    context = {
        "city": city_asked,
        "city_url": city_asked.city_url,
        "center": center,
        "coordinates": coordinates,
        "categories": categories_asked,
        "maps_api": settings.GMAPS_API,
    }

    template = loader.get_template('please_website_app/ville.html')
    return HttpResponse(template.render(context, request))


def merci(request):

    quotes_nb = Quote.objects.all().count()

    nb = int(randint(1, quotes_nb))
    quote = Quote.objects.get(id=nb)

    context = {
        "quote": quote,
    }

    template = loader.get_template('please_website_app/merci.html')
    return HttpResponse(template.render(context, request))


def commercants(request):

    context = {
    }
    template = loader.get_template('please_website_app/commercants.html')
    return HttpResponse(template.render(context, request))


def livreurs(request):

    context = {
    }
    template = loader.get_template('please_website_app/livreurs.html')
    return HttpResponse(template.render(context, request))


def candidature(request):

    if request.method == 'POST':
        form = forms.CandidateForm(data=request.POST)

        if form.is_valid():
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            phone = form.cleaned_data["phone"]
            email_candidate = form.cleaned_data["email"]
            linkedin = form.cleaned_data["linkedin"]
            message = form.cleaned_data["message"]

            # NOTIF EMAIL
            send_email(
                context={
                    "first_name": first_name,
                    "last_name": last_name,
                    "email": email_candidate,
                    "phone": phone,
                    "linkedin": linkedin,
                    "message": message,
                },
                from_address="contact@pleaseapp.com",
                to_address="contact@pleaseapp.com",
                reply_to_address=email_candidate,
                subject="Site Pro - Nouvelle Candidature Spontanée",
                template=loader.get_template('please_website_app/email_templates/en_candidature_spont'),
            )

            print('redirect to merci')

            return redirect('merci')

    else:
        form = forms.CandidateForm()

    context = {
        "form_candidate": forms.CandidateForm(),
    }

    template = loader.get_template('please_website_app/candidature.html')
    return HttpResponse(template.render(context, request))


def devenir_cm(request):

    if request.method == 'POST':

        form = forms.CityManagerForm(data=request.POST)

        if form.is_valid():
            first_name = form.cleaned_data["first_name"].capitalize()
            last_name = form.cleaned_data["last_name"].capitalize()
            city = form.cleaned_data["city"]
            phone = form.cleaned_data["phone"].replace(" ", "").replace(".", "").replace("-", "").replace("+", "")
            email_cm = form.cleaned_data["email"]
            password = form.cleaned_data["password"]

            User.objects.create_user(
                email=email_cm,
                password=password,
                username=email_cm,
            )

            CandidateCityManager(
                user=User.objects.get(username=email_cm),
                city=city,
                email=email_cm,
                first_name=first_name,
                last_name=last_name,
                phone=phone,
            ).save()

            user = authenticate(username=email_cm, password=password)
            login(request, user)

            # NOTIF EMAIL
            send_email(
                context={
                    "first_name": first_name,
                    "last_name": last_name,
                    "email": email_cm,
                    "phone": phone,
                },
                from_address="contact@pleaseapp.com",
                to_address="contact@pleaseapp.com",
                reply_to_address=email_cm,
                subject="Site Pro - Nouveau City Manager",
                template=loader.get_template('please_website_app/email_templates/en_cm_new'),
            )

            # CITY MANAGER EMAIL
            msg = EmailMessage(
                str("Votre inscription sur l'Espace Franchisé"),
                str(render_to_string('please_website_app/email_templates/ext_cm_welcome.html',
                                     {"first_name": first_name})),
                "Alexandre de Please <alexandre.dubois@pleaseapp.com>",
                [email_cm],
            )
            msg.content_subtype = "html"  # Main content is now text/html
            msg.send()

            return redirect('merci_inscription')

        else:
            print("Form not Valid")

    else:
        context = {
            "form_cm": forms.CityManagerForm(),
        }

        template = loader.get_template('please_website_app/devenir_cm.html')
        return HttpResponse(template.render(context, request))


def merci_signup(request):
    if request.user.is_authenticated and (CandidateCityManager.objects.filter(user=request.user).count() == 1):
        context = {
            "city": CandidateCityManager.objects.filter(user=request.user).first().city,
        }

        template = loader.get_template('please_website_app/merci_inscription.html')
        return HttpResponse(template.render(context, request))

    else:
        return redirect("login")


def login_cm(request):

    if request.user.is_authenticated:
        return redirect("app")
    else:
        form_class = forms.LoginForm

        if request.method == 'POST':
            form = form_class(data=request.POST)

            if form.is_valid():
                email_cm = form.cleaned_data["email"]
                password = form.cleaned_data["password"]

                user = authenticate(request, username=email_cm, password=password)

                if user is not None:
                    login(request, user=user)
                    return redirect('app')
                else:
                    return redirect('login')

    context = {
        "form": forms.LoginForm(),
    }

    template = loader.get_template('please_website_app/login.html')
    return HttpResponse(template.render(context, request))


# APP SECTION
def app(request):
    if not request.user.is_authenticated:
        return redirect("login")
    else:
        candidate = CandidateCityManager.objects.get(user=request.user)

        form_project = forms.ProjectForm

        if request.method == 'POST':
            form = form_project(data=request.POST)

            if form.is_valid():
                project = form.cleaned_data["project"]
                apport = form.cleaned_data["apport"]

                candidate.project = project
                candidate.apport = apport
                candidate.save()

    context = {
        "candidate": candidate,
        "form_project": form_project(
            initial={
                "project": candidate.project,
                "apport": candidate.apport,
            }
        ),
    }

    template = loader.get_template('please_website_app/app.html')
    return HttpResponse(template.render(context, request))


def app_2(request):
    if not request.user.is_authenticated:
        return redirect("login")
    else:
        candidate = CandidateCityManager.objects.get(user=request.user)
        form_city = forms.CityForm

        if request.method == 'POST':
            form = form_city(data=request.POST)

            if form.is_valid():
                area = form.cleaned_data["area"]
                inhabitants = form.cleaned_data["inhabitants"]
                density = form.cleaned_data["density"]
                main_housing_rate = form.cleaned_data["main_housing_rate"]
                unemployment = form.cleaned_data["unemployment"]
                activity = form.cleaned_data["activity"]
                net_salary_average = form.cleaned_data["net_salary_average"]
                restaurants = form.cleaned_data["restaurants"]
                bakeries = form.cleaned_data["bakeries"]
                shops_food = form.cleaned_data["shops_food"]
                shops_service = form.cleaned_data["shops_service"]
                competition = form.cleaned_data["competition"]

                candidate.area = area
                candidate.inhabitants = inhabitants
                candidate.density = density
                candidate.main_housing_rate = main_housing_rate
                candidate.unemployment = unemployment
                candidate.activity = activity
                candidate.net_salary_average = net_salary_average
                candidate.restaurants = restaurants
                candidate.bakeries = bakeries
                candidate.shops_food = shops_food
                candidate.shops_service = shops_service
                candidate.competition = competition
                candidate.save()

        context = {
            "candidate": candidate,
            "form": form_city(
                initial={
                    "area": candidate.city if not candidate.area else candidate.area,
                    "inhabitants": candidate.inhabitants,
                    "density": candidate.density,
                    "main_housing_rate": candidate.main_housing_rate,
                    "unemployment": candidate.unemployment,
                    "activity": candidate.activity,
                    "net_salary_average": candidate.net_salary_average,
                    "restaurants": candidate.restaurants,
                    "bakeries": candidate.bakeries,
                    "shops_food": candidate.shops_food,
                    "shops_service": candidate.shops_service,
                    "competition": candidate.competition,
                }
            ),
        }
        template = loader.get_template('please_website_app/app_2.html')
        return HttpResponse(template.render(context, request))


def app_3(request):
    if not request.user.is_authenticated:
        return redirect("login")
    else:
        candidate = CandidateCityManager.objects.get(user=request.user)
        form_curriculum = forms.CurriculumForm

        if request.method == 'POST':
            form = form_curriculum(request.POST)

            if form.is_valid():
                availability = form.cleaned_data["availability"]
                curriculum = form.cleaned_data["curriculum"]
                linkedin = form.cleaned_data["linkedin"]

                candidate.availability = availability
                candidate.curriculum = curriculum
                candidate.linkedin = linkedin
                candidate.save()

        context = {
            "candidate": candidate,
            "form_curriculum": form_curriculum(
                initial={
                    "availability": candidate.availability,
                    "curriculum": candidate.curriculum,
                    "linkedin": candidate.linkedin,
                }
            ),
        }

        template = loader.get_template('please_website_app/app_3.html')
        return HttpResponse(template.render(context, request))


def app_commerce(request):
    if not request.user.is_authenticated:
        return redirect("login")
    else:
        pass

    candidate = CandidateCityManager.objects.get(user=request.user)

    form_commerce = forms.MerchantForm

    if request.method == 'POST':
        form = form_commerce(data=request.POST)

        if form.is_valid():
            Merchant(
                city_manager=candidate,
                first_name=form.cleaned_data["first_name"],
                last_name=form.cleaned_data["last_name"],
                business_name=form.cleaned_data["business_name"],
                interested=form.cleaned_data["interested"],
                competition=form.cleaned_data["competition"],
                delivery=form.cleaned_data["delivery"],
                phone=form.cleaned_data["phone"],
                email=form.cleaned_data["email"],
                business_type=form.cleaned_data["business_type"],
            ).save()

            return redirect('app_2')

    context = {
        "candidate": candidate,
        "form_merchant": form_commerce,
    }

    template = loader.get_template('please_website_app/app_commerce.html')
    return HttpResponse(template.render(context, request))


def app_livreur(request):
    if not request.user.is_authenticated:
        return redirect("login")
    else:
        pass

    candidate = CandidateCityManager.objects.get(user=request.user)

    form_livreur = forms.DeliveryManForm

    if request.method == 'POST':
        form = form_livreur(data=request.POST)

        if form.is_valid():
            DeliveryMan(
                city_manager=candidate,
                first_name=form.cleaned_data["first_name"],
                last_name=form.cleaned_data["last_name"],
                phone=form.cleaned_data["phone"],
                email=form.cleaned_data["email"],
                siret=form.cleaned_data["siret"],
                auto=form.cleaned_data["auto"],
                sent_to_bereglo=form.cleaned_data["sent_to_bereglo"],
            ).save()

            return redirect('app_3')

    context = {
        "candidate": candidate,
        "form_delivery_man": form_livreur,
    }

    template = loader.get_template('please_website_app/app_livreur.html')
    return HttpResponse(template.render(context, request))


# CONTACT FORMS

def contact(request):

    if request.method == 'POST':
        form = forms.ContactForm(data=request.POST)
        print(form)

        if form.is_valid():
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            phone = form.cleaned_data["phone"]
            email_contact = form.cleaned_data["email"]
            message = form.cleaned_data["message"]

            print(message)

            LogContactForm(
                first_name=first_name,
                last_name=last_name,
                phone=phone,
                email=email_contact,
                message=message,
                date=datetime.datetime.now(),
            ).save()

            # NOTIF EMAIL
            send_email(
                context={
                    "first_name": first_name,
                    "last_name": last_name,
                    "email": email_contact,
                    "phone": phone,
                    "message": message,
                },
                from_address="contact@pleaseapp.com",
                to_address="contact@pleaseapp.com",
                reply_to_address=email_contact,
                subject="Site Pro - Nouveau Contact",
                template=loader.get_template('please_website_app/email_templates/en_contact'),
            )

            print('redirect to merci')

            return redirect('merci')

    else:
        form = forms.ContactForm()

    context = {
        "form_contact": forms.ContactForm(),
    }

    template = loader.get_template('please_website_app/contact.html')
    return HttpResponse(template.render(context, request))


def contact_cm(request):

    if request.method == 'POST':
        form = forms.ContactFormCm(data=request.POST)
        print(form)

        if form.is_valid():
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            phone = form.cleaned_data["phone"]
            email_contact = form.cleaned_data["email"]
            message = form.cleaned_data["message"]
            city = form.cleaned_data["city"]

            LogContactForm(
                first_name=first_name,
                last_name=last_name,
                phone=phone,
                email=email_contact,
                message=message,
                date=datetime.datetime.now(),
            ).save()

            # NOTIF EMAIL
            send_email(
                context={
                    "first_name": first_name,
                    "last_name": last_name,
                    "email": email_contact,
                    "phone": phone,
                    "message": message,
                },
                from_address="contact@pleaseapp.com",
                to_address="contact@pleaseapp.com",
                reply_to_address=email_contact,
                subject=str("Site Pro - Nouveau Candidat à Recontacter " + city),
                template=loader.get_template('please_website_app/email_templates/en_contact'),
            )

            print('redirect to merci')

            return redirect('merci')

    else:
        form = forms.ContactFormCm()

    context = {
        "form_contact": forms.ContactFormCm(),
    }

    template = loader.get_template('please_website_app/contact_cm.html')
    return HttpResponse(template.render(context, request))


def contact_city(request):

    if request.method == 'POST':
        form = forms.ContactFormCity(data=request.POST)

        if form.is_valid():
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            phone = form.cleaned_data["phone"]
            email_contact = form.cleaned_data["email"]
            city = form.cleaned_data["city"]
            position = form.cleaned_data["position"]
            message = form.cleaned_data["message"]

            LogContactFormCity(
                first_name=first_name,
                last_name=last_name,
                phone=phone,
                email=email_contact,
                city=city,
                position=position,
                message=message,
                date=datetime.datetime.now(),
            ).save()

            # NOTIF EMAIL
            send_email(
                context={
                    "first_name": first_name,
                    "last_name": last_name,
                    "email": email_contact,
                    "phone": phone,
                    "city": city,
                    "position": position,
                    "message": message,
                },
                from_address="contact@pleaseapp.com",
                to_address="contact@pleaseapp.com",
                reply_to_address=email_contact,
                subject="Site Pro - Nouveau Contact Collectivité",
                template=loader.get_template('please_website_app/email_templates/en_contact_collectivite'),
            )

            print('redirect to merci')

            return redirect('merci')

    else:

        form = forms.ContactFormCity()

    context = {
        "form_city": form,
    }

    template = loader.get_template('please_website_app/contact_collectivite.html')
    return HttpResponse(template.render(context, request))


def contact_merchant(request):

    if request.method == 'POST':
        form = forms.ContactFormMerchant(data=request.POST)

        if form.is_valid():
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            phone = form.cleaned_data["phone"]
            email_contact = form.cleaned_data["email"]
            city = form.cleaned_data["city"]
            business_name = form.cleaned_data["business_name"]
            siret = form.cleaned_data["siret"]
            message = form.cleaned_data["message"]

            LogContactFormMerchant(
                first_name=first_name,
                last_name=last_name,
                phone=phone,
                email=email_contact,
                city=city,
                business_name=business_name,
                siret=siret,
                message=message,
                date=datetime.datetime.now(),
            ).save()

            # NOTIF EMAIL
            send_email(
                context={
                    "first_name": first_name,
                    "last_name": last_name,
                    "email": email_contact,
                    "phone": phone,
                    "city": city,
                    "business_name": business_name,
                    "siret": siret,
                    "message": message,
                },
                from_address="contact@pleaseapp.com",
                to_address="contact@pleaseapp.com",
                reply_to_address=email_contact,
                subject="Site Pro - Nouveau Contact Commerçant",
                template=loader.get_template('please_website_app/email_templates/en_contact_commercant'),
            )

            print('redirect to merci')

            return redirect('merci')

    else:

        form = forms.ContactFormMerchant()

    context = {
        "form_merchant": form,
    }

    template = loader.get_template('please_website_app/contact_commercant.html')
    return HttpResponse(template.render(context, request))


def contact_delivery(request):

    if request.method == 'POST':
        form = forms.ContactFormDeliveryMan(data=request.POST)

        if form.is_valid():
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            phone = form.cleaned_data["phone"]
            email_contact = form.cleaned_data["email"]
            city = form.cleaned_data["city"]
            message = form.cleaned_data["message"]

            LogContactFormDelivery(
                first_name=first_name,
                last_name=last_name,
                phone=phone,
                email=email_contact,
                city=city,
                message=message,
                date=datetime.datetime.now(),
            ).save()

            # NOTIF EMAIL
            send_email(
                context={
                    "first_name": first_name,
                    "last_name": last_name,
                    "email": email_contact,
                    "phone": phone,
                    "city": city,
                    "message": message,
                },
                from_address="contact@pleaseapp.com",
                to_address="contact@pleaseapp.com",
                reply_to_address=email_contact,
                subject="Site Pro - Nouveau Contact Livreur",
                template=loader.get_template('please_website_app/email_templates/en_contact_livreur'),
            )

            print('redirect to merci')

            return redirect('merci')

    else:

        form = forms.ContactFormDeliveryMan()

    context = {
        "form_delivery": form,
    }

    template = loader.get_template('please_website_app/contact_livreur.html')

    return HttpResponse(template.render(context, request))


def logout_app(request):
    logout(request)

    return redirect('login')


def task_completed(request):
    if not request.user.is_authenticated:
        return redirect("login")
    else:
        candidate = CandidateCityManager.objects.get(user=request.user)

        candidate.task_completed = True
        candidate.save()

        # NOTIF EMAIL
        send_email(
            context={
                "first_name": candidate.first_name,
                "last_name": candidate.last_name,
                "email": candidate.email,
                "phone": candidate.phone,
                "project": candidate.project,
                "apport": candidate.apport,
                "area": candidate.area,
                "inhabitants": candidate.inhabitants,
                "density": candidate.density,
                "main_housing_rate": candidate.main_housing_rate,
                "unemployment": candidate.unemployment,
                "activity": candidate.activity,
                "net_salary_average": candidate.net_salary_average,
                "restaurants": candidate.restaurants,
                "bakeries": candidate.bakeries,
                "shops_food": candidate.shops_food,
                "shops_service": candidate.shops_service,
                "competition": candidate.competition,
            },
            from_address="contact@pleaseapp.com",
            to_address="contact@pleaseapp.com",
            reply_to_address=candidate.email,
            subject="Site Pro - Etude de Marché Validée",
            template=loader.get_template('please_website_app/email_templates/en_cm_validated'),
        )

        return redirect('merci')


def nps(request):

    context = {}
    template = loader.get_template('please_website_app/nps.html')
    return HttpResponse(template.render(context, request))


def handler404(request, exception=None,  template_name='please_website_app/404.html'):
    context = {}
    template = loader.get_template('please_website_app/404.html')
    return HttpResponse(template.render(context, request))


def handler500(request, exception=None,  template_name='please_website_app/404.html'):
    context = {}
    template = loader.get_template('please_website_app/404.html')
    return HttpResponse(template.render(context, request))
