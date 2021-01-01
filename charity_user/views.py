from django.http import Http404
from django.shortcuts import render

# Create your views here.
from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import action
from charity_user.models import CharityUser
from charity_user.serializers import CharityUserSerializer
from newsletter_topic.models import NewsletterTopic
from newsletter_topic.serializers import NewsletterTopicSerializer


class CharityUserViewSet(viewsets.ModelViewSet):
    queryset = CharityUser.objects.all()
    serializer_class = CharityUserSerializer

class SubscribedNewsletterTopicsViewSet(viewsets.ModelViewSet):
    queryset = NewsletterTopic.objects.all()
    serializer_class = NewsletterTopicSerializer
