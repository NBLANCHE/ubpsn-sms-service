from rest_framework import serializers

from charity_user.models import CharityUser
from newsletter_topic.models import NewsletterTopic


class SubscribedNewsletterTopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsletterTopic
        fields = ["id", "name"]


class CharityUserSerializer(serializers.ModelSerializer):
    subscribed_newsletter_topics = SubscribedNewsletterTopicSerializer(
        many=True, read_only=True
    )

    class Meta:
        model = CharityUser
        fields = ["id", "name", "phone_number", "subscribed_newsletter_topics"]
