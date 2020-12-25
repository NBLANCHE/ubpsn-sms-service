from django.contrib import admin
from newsletter_topic.models import NewsletterTopic, NewsletterTopicMessage

# Register your models here.
admin.site.register(NewsletterTopic)
admin.site.register(NewsletterTopicMessage)
