# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from datetime import date


class Article(models.Model):

    logo_white = models.ImageField(blank=True, null=True, upload_to="documents/article/white_logos")
    logo_grey = models.ImageField(blank=True, null=True, upload_to="documents/article/grey_logos")
    logo_color = models.ImageField(blank=True, null=True, upload_to="documents/article/color_logos")
    title = models.CharField(max_length=500, blank=True, null=True)
    abstract = models.CharField(max_length=120, blank=True, null=True)
    link = models.CharField(max_length=500, blank=True, null=True)
    top = models.BooleanField(null=True)

    # Auto Timestamp Generation
    created_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    modified_date = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return self.title


class City(models.Model):

    name = models.CharField(max_length=500, blank=True, null=True)
    description = models.TextField(max_length=500, blank=True, null=True)
    cover_image = models.ImageField(blank=True, null=True, upload_to="documents/city/")
    cm_image = models.ImageField(blank=True, null=True, upload_to="documents/city/")
    press_release = models.FileField(blank=True, null=True)
    link_to_store = models.CharField(max_length=500, blank=True, null=True)
    conciergerie_id = models.IntegerField(blank=True, null=True)
    gps_coordinates = models.CharField(max_length=500000, blank=True, null=True)
    gps_coordinates_lat = models.FloatField(blank=True, null=True)
    gps_coordinates_long = models.FloatField(blank=True, null=True)
    city_url = models.CharField(max_length=500, blank=True, null=True)

    # Auto Timestamp Generation
    created_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    modified_date = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    city = models.ForeignKey(City, blank=True, null=True, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=500, blank=True, null=True)
    image = models.ImageField(blank=True, null=True, upload_to="documents/category/")

    # Auto Timestamp Generation
    created_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    modified_date = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return str(self.city.name + " - " + self.name)


class CityManager(models.Model):

    partner_last_name = models.CharField(max_length=500, blank=True, null=True)
    partner_first_name = models.CharField(max_length=500, blank=True, null=True)
    email = models.CharField(max_length=500, blank=True, null=True)
    phone = models.CharField(max_length=500, blank=True, null=True)
    abstract = models.TextField(max_length=150, blank=True, null=True)
    testimonial = models.TextField(max_length=5000, blank=True, null=True)
    city_name = models.CharField(max_length=100, blank=True, null=True)
    profile_picture = models.ImageField(blank=True, null=True, upload_to="documents/testimonials/")
    video_link = models.CharField(max_length=500, blank=True, null=True)

    # Auto Timestamp Generation
    created_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    modified_date = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return self.partner_last_name


class TeamMember(models.Model):

    name = models.CharField(max_length=500, blank=True, null=True)
    role = models.CharField(max_length=500, blank=True, null=True)
    phone = models.CharField(max_length=500, blank=True, null=True)
    display_rank = models.IntegerField(blank=True, null=True)
    profile_picture = models.ImageField(blank=True, null=True, upload_to="documents/team/")
    email = models.CharField(max_length=500, blank=True, null=True)
    linkedin = models.CharField(max_length=500, blank=True, null=True)
    facebook = models.CharField(max_length=500, blank=True, null=True)
    google = models.CharField(max_length=500, blank=True, null=True)

    # Auto Timestamp Generation
    created_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    modified_date = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return self.name


class Job(models.Model):

    Marketing = "Marketing & Sales"
    Tech = "Tech"
    Product = "Product"
    Operations = "Operations"
    Admin = "Admin"

    Intern = "Intern"
    Full_Time = "Full-Time"

    position_type_choices = ((Intern, "Intern"),
                             (Full_Time, "Full-Time"))

    category_choices = ((Marketing, "Marketing & Sales"),
                        (Tech, "Tech"),
                        (Product, "Product"),
                        (Operations, "Operations"),
                        (Admin, "Admin"))

    position = models.CharField(max_length=500, blank=True, null=True)
    position_type = models.CharField(max_length=20, choices=position_type_choices, default=Full_Time)
    city = models.CharField(max_length=500, blank=True, null=True)
    country = models.CharField(max_length=500, blank=True, null=True)
    abstract = models.CharField(max_length=500, blank=True, null=True)
    category = models.CharField(max_length=20, choices=category_choices, default=Marketing)
    link = models.CharField(max_length=500, blank=True, null=True)

    # Auto Timestamp Generation
    created_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    modified_date = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return self.position


class Document(models.Model):
    name = models.CharField(max_length=500, blank=True, null=True)
    file = models.FileField(blank=True, null=True, upload_to="documents/site/")

    # Auto Timestamp Generation
    created_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    modified_date = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return self.name


class CandidateCityManager(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    first_name = models.CharField(max_length=500, blank=True, null=True)
    last_name = models.CharField(max_length=500, blank=True, null=True)
    city = models.CharField(max_length=500, blank=True, null=True)
    phone = models.CharField(max_length=500, blank=True, null=True)
    email = models.EmailField(max_length=500, blank=True, null=True)
    task_completed = models.BooleanField(null=True)

    project = models.TextField(max_length=5000)
    apport = models.IntegerField(blank=True, null=True)

    area = models.CharField(max_length=500, blank=True, null=True)
    inhabitants = models.IntegerField(blank=True, null=True)
    density = models.FloatField(blank=True, null=True)
    main_housing_rate = models.FloatField(blank=True, null=True)
    unemployment = models.FloatField(blank=True, null=True)
    activity = models.FloatField(blank=True, null=True)
    net_salary_average = models.FloatField(blank=True, null=True)
    restaurants = models.IntegerField(blank=True, null=True)
    bakeries = models.IntegerField(blank=True, null=True)
    shops_food = models.IntegerField(blank=True, null=True)
    shops_service = models.IntegerField(blank=True, null=True)
    competition = models.CharField(max_length=500, blank=True, null=True)

    AVAILABILITY_CHOICES = (
        (1, 'Immédiate'),
        (2, 'Dans les 1 à 3 mois'),
        (3, 'Dans les 3 à 6 mois'),
        (4, 'Dans plus de 6 mois'),
    )

    availability = models.IntegerField(
        choices=AVAILABILITY_CHOICES,
        default=1,
    )
    curriculum = models.TextField(max_length=5000)
    linkedin = models.CharField(max_length=500, blank=True, null=True)
    cv = models.FileField(blank=True, null=True, upload_to="documents/cv/")

    traffic_source = models.CharField(max_length=500, blank=True, null=True)

    # Auto Timestamp Generation
    created_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    modified_date = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return str(self.first_name + " " + self.last_name)


class DeliveryMan(models.Model):
    city_manager = models.ForeignKey(CandidateCityManager, on_delete=models.DO_NOTHING)
    first_name = models.CharField(max_length=500, blank=True, null=True)
    last_name = models.CharField(max_length=500, blank=True, null=True)
    picture = models.ImageField(blank=True, null=True, upload_to="documents/delivery_man/")
    phone = models.CharField(max_length=500, blank=True, null=True)
    email = models.EmailField(max_length=500, blank=True, null=True)
    siret = models.CharField(max_length=500, blank=True, null=True)
    auto = models.BooleanField(null=True)
    sent_to_bereglo = models.BooleanField(null=True)

    # Auto Timestamp Generation
    created_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    modified_date = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return str(self.first_name + " " + self.last_name + " - " + self.city_manager.last_name)


class Merchant(models.Model):

    category_choices = (
        ("Restaurant", "Restaurant"),
        ("Fast Food", "Fast Food"),
        ("Bien-Etre & Beauté", "Bien-Etre & Beauté"),
        ("Boulangerie & Petit-Déjeuner", "Boulangerie & Petit-Déjeuner"),
        ("Epicerie de Quartier", "Epicerie de Quartier"),
        ("Epicerie Fine", "Epicerie Fine"),
        ("Course et Marché", "Course et Marché"),
        ("Gourmandises", "Gourmandises"),
        ("Service", "Service"),
    )

    city_manager = models.ForeignKey(CandidateCityManager, on_delete=models.DO_NOTHING)
    first_name = models.CharField(max_length=500, blank=True, null=True)
    last_name = models.CharField(max_length=500, blank=True, null=True)
    picture = models.ImageField(blank=True, null=True, upload_to="documents/merchant/")
    business_name = models.CharField(max_length=500, blank=True, null=True)
    phone = models.CharField(max_length=500, blank=True, null=True)
    email = models.EmailField(max_length=500, blank=True, null=True)
    business_type = models.CharField(max_length=500, choices=category_choices, default="Restaurant")
    interested = models.CharField(max_length=500, blank=True, null=True)
    competition = models.BooleanField(null=True)
    delivery = models.BooleanField(null=True)

    # Auto Timestamp Generation
    created_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    modified_date = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return str(self.business_name + " - " + self.city_manager.last_name)


class LogLeadForm(models.Model):
    email = models.EmailField(blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)
    zip_code = models.CharField(max_length=5, blank=True, null=True)

    # Auto Timestamp Generation
    created_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    modified_date = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return self.email


class LogSendSms(models.Model):
    phone = models.CharField(max_length=500, blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)

    # Auto Timestamp Generation
    created_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    modified_date = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return self.phone


class LogContactForm(models.Model):
    first_name = models.CharField(max_length=500, blank=True, null=True)
    last_name = models.CharField(max_length=500, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=500, blank=True, null=True)
    message = models.CharField(max_length=5000, blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)

    # Auto Timestamp Generation
    created_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    modified_date = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return str(self.first_name + " " + self.last_name)


class LogContactFormDelivery(models.Model):
    first_name = models.CharField(max_length=500, blank=True, null=True)
    last_name = models.CharField(max_length=500, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=500, blank=True, null=True)
    city = models.CharField(max_length=500, blank=True, null=True)
    message = models.CharField(max_length=5000, blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)

    # Auto Timestamp Generation
    created_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    modified_date = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return str(self.first_name + " " + self.last_name)


class LogContactFormCity(models.Model):
    first_name = models.CharField(max_length=500, blank=True, null=True)
    last_name = models.CharField(max_length=500, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=500, blank=True, null=True)
    city = models.CharField(max_length=500, blank=True, null=True)
    position = models.CharField(max_length=500, blank=True, null=True)
    message = models.CharField(max_length=5000, blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)

    # Auto Timestamp Generation
    created_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    modified_date = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return str(self.first_name + " " + self.last_name)


class LogContactFormMerchant(models.Model):
    first_name = models.CharField(max_length=500, blank=True, null=True)
    last_name = models.CharField(max_length=500, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=500, blank=True, null=True)
    city = models.CharField(max_length=500, blank=True, null=True)
    business_name = models.CharField(max_length=500, blank=True, null=True)
    siret = models.CharField(max_length=500, blank=True, null=True)
    message = models.CharField(max_length=5000, blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)

    # Auto Timestamp Generation
    created_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    modified_date = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return str(self.first_name + " " + self.last_name)


class Quote(models.Model):
    quote = models.TextField(max_length=5000, blank=True, null=True)
    author = models.CharField(max_length=500, blank=True, null=True)

    # Auto Timestamp Generation
    created_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    modified_date = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return self.author
