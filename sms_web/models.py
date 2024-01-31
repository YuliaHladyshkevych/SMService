from django.db import models


class SendSMS(models.Model):
    phone = models.CharField(max_length=15)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "sms"
        ordering = ["-timestamp"]

    def __str__(self):
        return f"{self.phone} - {self.timestamp}"
