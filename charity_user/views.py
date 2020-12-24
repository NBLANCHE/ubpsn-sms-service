from django.http import Http404
from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from charity_user.models import CharityUser
from charity_user.serializers import CharityUserSerializer
from newsletter_topic.models import NewsletterTopic
from newsletter_topic.serializers import NewsletterTopicSerializer


class CharityUserList(APIView):
    def get(self, request, format=None):
        charity_user = CharityUser.objects.all()
        serializer = CharityUserSerializer(charity_user, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CharityUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CharityUserDetail(APIView):
    def get_object(self, pk):
        try:
            return CharityUser.objects.get(pk=pk)
        except CharityUser.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        charity_user = self.get_object(pk)
        serializer = CharityUserSerializer(charity_user)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        charity_user = self.get_object(pk)
        serializer = CharityUserSerializer(charity_user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        charity_user = self.get_object(pk)
        charity_user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CharityUserSubscribedNewsletterTopicDetail(APIView):
    def get_charity_user(self, charity_user_pk) -> CharityUser:
        try:
            return CharityUser.objects.get(pk=charity_user_pk)
        except CharityUser.DoesNotExist:
            raise Http404

    def get_newsletter_topic(self, newsletter_topic_pk) -> NewsletterTopic:
        try:
            return NewsletterTopic.objects.get(pk=newsletter_topic_pk)
        except NewsletterTopic.DoesNotExist:
            raise Http404

    def post(self, request, charity_user_pk, newsletter_topic_pk, format=None):
        charity_user = self.get_charity_user(charity_user_pk)
        newsletter_topic = self.get_newsletter_topic(newsletter_topic_pk)

        charity_user.subscribed_newsletter_topics.add(newsletter_topic)
        charity_user.save()
        serializer = CharityUserSerializer(charity_user)
        return Response(serializer.data)

    def delete(self, request, charity_user_pk, newsletter_topic_pk, format=None):
        charity_user = self.get_charity_user(charity_user_pk)
        newsletter_topic = self.get_newsletter_topic(newsletter_topic_pk)

        charity_user.subscribed_newsletter_topics.remove(newsletter_topic)
        charity_user.save()
        serializer = CharityUserSerializer(charity_user)
        return Response(serializer.data)
