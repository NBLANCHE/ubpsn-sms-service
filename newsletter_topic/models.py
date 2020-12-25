from django.db import models


class NewsletterTopic(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class NewsletterTopicMessage(models.Model):
    message = models.CharField(max_length=255)
    newsletter_topic = models.ForeignKey(
        NewsletterTopic, on_delete=models.CASCADE, related_name="messages"
    )

    def __str__(self):
        return self.message
