from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from twilio.rest import Client

from sms.models import SendSMS
from sms_service import settings


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
            print("Sending SMS")
            message = client.messages.create(
                body=message,
                from_="+12256358610",
                to=phone,
            )
            SendSMS.objects.create(phone=phone, message=message.body)
            return JsonResponse(
                {"status": "success",
                 "message": f"SMS sent successfully to {phone}"}
            )
        except Exception as e:
            print(str(e))
            return JsonResponse({'status': 'error', 'message': str(e)})

    return JsonResponse(
        {"status": "error", "message": "Invalid request method"}
    )
