from django.urls import path

from sms.views import home

urlpatterns = [
    path('home/', home, name="home"),
]
