from django.http import Http404

# Create your views here.
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from newsletter_topic.models import NewsletterTopic, NewsletterTopicMessage
from newsletter_topic.serializers import NewsletterTopicSerializer, NewsletterTopicMessageSerializer


class NewsletterTopicList(APIView):
    def get(self, request, format=None):
        newsletter_topics = NewsletterTopic.objects.all()
        serializer = NewsletterTopicSerializer(newsletter_topics, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = NewsletterTopicSerializer(data=request.data)
        if (serializer.is_valid()):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class NewsletterTopicDetail(APIView):
    def get_object(self, pk):
        try:
            return NewsletterTopic.objects.get(pk=pk)
        except NewsletterTopic.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        newsletter_topic = self.get_object(pk)
        serializer = NewsletterTopicSerializer(newsletter_topic)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        newsletter_topic = self.get_object(pk)
        serializer = NewsletterTopicSerializer(newsletter_topic, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        newsletter_topic = self.get_object(pk)
        newsletter_topic.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class NewsletterTopicMessageList(APIView):
    def get_object(self, pk):
        try:
            return NewsletterTopic.objects.get(pk=pk)
        except NewsletterTopic.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        newsletter_topic_messages = NewsletterTopicMessage.objects.filter(newsletter_topic=pk)
        serializer = NewsletterTopicMessageSerializer(newsletter_topic_messages, many=True)
        return Response(serializer.data)

    def post(self, request, pk, format=None):
        newsletter_topic = self.get_object(pk)
        serializer = NewsletterTopicMessageSerializer(data=request.data)
        if (serializer.is_valid()):
            serializer.save(newsletter_topic=newsletter_topic)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
