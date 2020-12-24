from django.db import models


# Create your models here.
from charity_user.models import CharityUser


class Message(models.Model):
    message = models.CharField(max_length=255)
    charity_user = models.ForeignKey(CharityUser, on_delete=models.CASCADE, related_name='messages')
