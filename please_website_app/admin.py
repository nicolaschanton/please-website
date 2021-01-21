# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from .models import Article, City, CityManager, TeamMember, Job, Document, LogSendSms, LogLeadForm, Category, \
    CandidateCityManager, Merchant, DeliveryMan, LogContactFormCity, LogContactFormMerchant, LogContactForm, \
    LogContactFormDelivery, Quote


@admin.register(CandidateCityManager)
class CandidateCityManagerAdmin(admin.ModelAdmin):
    search_fields = []
    list_filter = [
        "city",
        "created_date",
        "modified_date",
    ]
    list_display = [
        "first_name",
        "last_name",
        "city",
        "phone",
        "email",
        "traffic_source",
        "created_date",
        "modified_date",
    ]
    pass


@admin.register(LogContactFormDelivery)
class LogContactFormDeliveryAdmin(admin.ModelAdmin):
    search_fields = []
    list_filter = [
        "city",
        "created_date",
        "modified_date",
    ]
    list_display = [
        "first_name",
        "last_name",
        "email",
        "phone",
        "city",
        "date",
        "created_date",
        "modified_date",
    ]
    pass


@admin.register(LogContactFormMerchant)
class LogContactFormMerchantAdmin(admin.ModelAdmin):
    search_fields = []
    list_filter = []
    list_display = [
        "first_name",
        "last_name",
        "email",
        "phone",
        "city",
        "business_name",
        "created_date",
        "modified_date",
    ]
    pass


admin.site.register(Article)
admin.site.register(City)
admin.site.register(CityManager)
admin.site.register(TeamMember)
admin.site.register(Job)
admin.site.register(Document)
admin.site.register(LogSendSms)
admin.site.register(LogLeadForm)
admin.site.register(LogContactFormCity)
admin.site.register(LogContactForm)
admin.site.register(Category)
admin.site.register(Merchant)
admin.site.register(DeliveryMan)
admin.site.register(Quote)
