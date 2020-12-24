from django.db import models

# Create your models here.
from charity_user.models import CharityUser

from enum import Enum


class MessageStatus(Enum):
    CREATED = "Created"
    SENT = "Sent"
    DELIVERED = "Delivered"
    READ = "Read"
    FAILED = "Failed"


class Message(models.Model):
    message = models.CharField(max_length=255)
    charity_user = models.ForeignKey(
        CharityUser, on_delete=models.CASCADE, related_name="messages"
    )
    message_status = models.CharField(
        max_length=50, choices=[(status, status.value) for status in MessageStatus]
    )


class IncomingSms:
    def __init__(self, **kwargs):
        self.sms_sid = kwargs["MessageSid"]
        self.account_sid = kwargs["AccountSid"]
        self.from_number = kwargs["From"]
        self.from_city = kwargs["FromCity"]
        self.from_state = kwargs["FromState"]
        self.from_country = kwargs["FromCountry"]
        self.to_number = kwargs["To"]
        self.body = kwargs["Body"]
