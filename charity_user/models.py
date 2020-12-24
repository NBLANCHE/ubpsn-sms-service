from django.db import models

# Create your models here.
from newsletter_topic.models import NewsletterTopic


class CharityUser(models.Model):
    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)
    subscribed_newsletter_topics = models.ManyToManyField(
        NewsletterTopic, related_name="subscribed_users"
    )
