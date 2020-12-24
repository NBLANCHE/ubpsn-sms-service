from rest_framework import serializers

from newsletter_topic.models import NewsletterTopic, NewsletterTopicMessage


class NewsletterTopicMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsletterTopicMessage
        fields = ['id', 'message']


class NewsletterTopicSerializer(serializers.ModelSerializer):
    messages = NewsletterTopicMessageSerializer(many=True)

    class Meta:
        model = NewsletterTopic
        fields = ['id', 'name', 'messages']
