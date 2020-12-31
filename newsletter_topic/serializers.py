from rest_framework import serializers

from charity_user.models import CharityUser
from newsletter_topic.models import NewsletterTopic, NewsletterTopicMessage
from charity_user.serializers import CharityUserSerializer


class NewsletterTopicMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsletterTopicMessage
        fields = ["id", "message", "newsletter_topic"]


class SubscribedCharityUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CharityUser
        fields = ["id", "name", "phone_number"]


class NewsletterTopicSerializer(serializers.ModelSerializer):
    messages = NewsletterTopicMessageSerializer(
        many=True, required=False, read_only=True
    )
    subscribed_users = CharityUserSerializer(many=True, read_only=True)

    class Meta:
        model = NewsletterTopic
        fields = ["id", "name", "messages", "subscribed_users"]
