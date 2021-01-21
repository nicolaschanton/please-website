import django
django.setup()
import sys
from apscheduler.schedulers.blocking import BlockingScheduler
import requests
from please_website_app.models import Category, City
import os

sched = BlockingScheduler()


@sched.scheduled_job('cron', hour='10')
def update_categories():

    try:

        url_login = "https://mw.please-it.com/next-mw/login"

        headers_login = {
            'Accept': "application/json",
            'Cache-Control': "no-cache",
        }

        payload = {
            "username": "nicolas.chanton@gmail.com",
            "password": "Please2017",
        }

        response_login = requests.request("POST", url_login, headers=headers_login, data=payload).json()
        access_token = response_login.get("accessToken")

        for city in City.objects.all(conciergerie_id__isnull=False):
            try:
                mw_nb_id = city.conciergerie_id
                url = str("https://mw.please-it.com/next-mw/api/marketing/category/conciergerie/" + mw_nb_id)

                headers = {
                    'Accept': "application/json",
                    'Authorization': str("Bearer " + access_token),
                    'Cache-Control': "no-cache",
                }

                response = requests.request("GET", url, headers=headers).json()

                for category in response:

                    if Category.objects.get(city=city, name=category.get("title")) is None:

                        Category(
                            name=category.get("title"),
                            city=city,
                            image="",
                        )

                    else:
                        pass

            except:
                continue
    except:
        pass

    return


sched.start()
