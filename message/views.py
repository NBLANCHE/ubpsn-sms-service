# Create your views here.
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from message.models import Message
from message.serializers import (
    ViewMessageSerializer,
    CreateMessageSerializer,
    SmsRequestSerializer,
)
from message.services import MessageService

message_service = MessageService()


class MessageList(APIView):
    def get(self, request, format=None):
        messages = Message.objects.all()
        serializer = ViewMessageSerializer(messages, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CreateMessageSerializer(data=request.data)
        if serializer.is_valid():
            message = serializer.create(serializer.data)
            message = message_service.send_message(message)
            return Response(
                ViewMessageSerializer(message).data, status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TwilioWebhook(APIView):
    def post(self, request, format=None):
        print(request)
        serializer = SmsRequestSerializer(data=request.data)
        if serializer.is_valid():
            incoming_sms = serializer.create(serializer.data)
            response = message_service.receive_message(incoming_sms)
            return Response(
                response.to_xml(),
                content_type="application/xml",
                status=status.HTTP_201_CREATED,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
