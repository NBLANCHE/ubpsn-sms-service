from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from charity_user.models import CharityUser
from message.models import Message
from message.serializers import ViewMessageSerializer, CreateMessageSerializer


class MessageList(APIView):
    def get(self, request, format=None):
        messages = Message.objects.all()
        serializer = ViewMessageSerializer(messages, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CreateMessageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.create(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
