from rest_framework import serializers

from charity_user.models import CharityUser
from newsletter_topic.models import NewsletterTopic, NewsletterTopicMessage


class NewsletterTopicMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsletterTopicMessage
        fields = ['id', 'message']


class SubscribedCharityUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CharityUser
        fields = ['id', 'name', 'phone_number']


class NewsletterTopicSerializer(serializers.ModelSerializer):
    messages = NewsletterTopicMessageSerializer(many=True)
    subscribed_users = SubscribedCharityUserSerializer(many=True, read_only=True)

    class Meta:
        model = NewsletterTopic
        fields = ['id', 'name', 'messages', 'subscribed_users']
