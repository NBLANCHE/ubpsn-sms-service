from django.http import Http404

# Create your views here.
from rest_framework import status, generics, viewsets
from rest_framework.response import Response
import logging, pprint

from newsletter_topic.models import NewsletterTopic, NewsletterTopicMessage
from newsletter_topic.serializers import (
    NewsletterTopicSerializer,
    NewsletterTopicMessageSerializer,
)
from message.models import Message
from message.services import MessageService

logger = logging.getLogger(__name__)

class NewsletterTopicViewSet(viewsets.ModelViewSet):
    queryset = NewsletterTopic.objects.all()
    serializer_class = NewsletterTopicSerializer


class NewsletterTopicMessageViewSet(viewsets.ModelViewSet):
    queryset = NewsletterTopicMessage.objects.all()
    serializer_class = NewsletterTopicMessageSerializer
    # Get users subscribed, then call service
    def perform_create(self, serializer):
        # TODO error handling etc
        newsletter_topic = NewsletterTopic.objects.get(name=serializer.validated_data['newsletter_topic'])
        for user in newsletter_topic.subscribed_users.all(): 
            # create a message for each user
            message_text = serializer.validated_data["message"]
            message = Message(message=message_text)
            message.charity_user = user
            message_service = MessageService()
            message_response = message_service.send_message(message)
