"""please_website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_please_website_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_please_website_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from please_website_app import views
from django.views.generic import TemplateView
import django


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^please_website_app/', include('please_website_app.urls')),
    url(r'^', include('please_website_app.urls')),
    url(r'^robots\.txt$', TemplateView.as_view(template_name="please_website_app/robots.txt", content_type='text/plain')),
]

django.conf.urls.handler404 = views.handler404
django.conf.urls.handler500 = views.handler500
