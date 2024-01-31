from django.urls import path

from sms_web.views import home, send_sms

urlpatterns = [
    path("home/", home, name="home"),
    path("send-sms/", send_sms, name="send_sms"),
]

app_name = "sms_web"
