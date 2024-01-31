from django.urls import path

from sms.views import home, send_sms

urlpatterns = [
    path("", home, name="home"),
    path("send-sms/", send_sms, name="send_sms"),
]

app_name = "sms"
