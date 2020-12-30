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
        @action(detail=True, methods=['get', 'post'])
        def subscribed_newslettter_topic(self, request, pk=None):
            # if request.method == 'get':
            # charity_user = CharityUser.objects.filter(id=pk)
            # probably don't need the all()
            subscribed_newsletter_topics = self.get_object().subscribed_newsletter_topics.all()
            serializer = NewsletterTopicSerializer(subscribed_newsletter_topics, many=True, context={'request': request})
            return Response(serializer.data)

            # if request.method == 'post':
            #     pass

# class CharityUserSubscribedNewsletterTopicDetail(APIView):
#     def post(self, request, charity_user_pk, newsletter_topic_pk, format=None):
#         charity_user = self.get_charity_user(charity_user_pk)
#         newsletter_topic = self.get_newsletter_topic(newsletter_topic_pk)

#         charity_user.subscribed_newsletter_topics.add(newsletter_topic)
#         charity_user.save()
#         serializer = CharityUserSerializer(charity_user)
#         return Response(serializer.data)

#     def delete(self, request, charity_user_pk, newsletter_topic_pk, format=None):
#         charity_user = self.get_charity_user(charity_user_pk)
#         newsletter_topic = self.get_newsletter_topic(newsletter_topic_pk)

#         charity_user.subscribed_newsletter_topics.remove(newsletter_topic)
#         charity_user.save()
#         serializer = CharityUserSerializer(charity_user)
#         return Response(serializer.data)
