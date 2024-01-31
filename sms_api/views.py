import json
import logging

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from twilio.rest import Client

from sms_service import settings
from sms_web.models import SendSMS


@csrf_exempt
def send_sms_api(request):
    if request.method == "POST":

        data = json.loads(request.body.decode("utf-8"))
        phone = data.get("phone")
        message = data.get("message")
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
