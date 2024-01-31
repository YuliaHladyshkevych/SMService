import logging

from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from twilio.rest import Client

from sms_web.models import SendSMS
from sms_service import settings

logging.basicConfig(filename="logs", level=logging.INFO,
                    format="%(asctime)s %(message)s")


@csrf_exempt
def home(request):
    return render(request, "home.html")


@csrf_exempt
def send_sms(request):
    if request.method == "POST":

        phone = request.POST.get("phone")
        message = request.POST.get("message")
        client = Client(settings.TWILIO_ACCOUNT_SID,
                        settings.TWILIO_AUTH_TOKEN)

        try:
            message = client.messages.create(
                body=message,
                from_="+12256358610",
                to=phone,
            )
            SendSMS.objects.create(phone=phone, message=message.body)
            logging.info(f"SMS was successfully sent to {phone}")
            return JsonResponse(
                {"status": "success",
                 "message": f"SMS was successfully sent to {phone}"}
            )
        except Exception as e:
            logging.error(f"Error sending SMS to {phone}: {str(e)}")
            return JsonResponse({'status': 'error', 'message': str(e)})

    return JsonResponse(
        {"status": "error", "message": "Invalid request method"}
    )
