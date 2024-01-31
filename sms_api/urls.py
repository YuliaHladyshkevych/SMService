from django.urls import path

from sms_api.views import send_sms_api

urlpatterns = [
    path("api/v1/send-sms/", send_sms_api, name="send_sms_api"),
]

app_name = "sms_api"
