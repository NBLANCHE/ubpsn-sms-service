from django.http import Http404

# Create your views here.
from rest_framework import status, generics;
from rest_framework.response import Response
from rest_framework.views import APIView

from newsletter_topic.models import NewsletterTopic, NewsletterTopicMessage
from newsletter_topic.serializers import NewsletterTopicSerializer, NewsletterTopicMessageSerializer


class NewsletterTopicList(generics.ListCreateAPIView):
    queryset = NewsletterTopic.objects.all()
    serializer_class = NewsletterTopicSerializer

class NewsletterTopicDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = NewsletterTopic.objects.all()
    serializer_class = NewsletterTopicSerializer

class NewsletterTopicMessageList(generics.ListCreateAPIView):
    queryset = NewsletterTopicMessage.objects.all()
    serializer_class = NewsletterTopicMessage