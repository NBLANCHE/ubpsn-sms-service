from django.db import models


# Create your models here.


class NewsletterTopic(models.Model):
    name = models.CharField(max_length=255)


class NewsletterTopicMessage(models.Model):
    message = models.CharField(max_length=255)
    newsletter_topic = models.ForeignKey(NewsletterTopic, on_delete=models.CASCADE, related_name='messages')
