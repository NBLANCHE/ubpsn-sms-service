from rest_framework import serializers

from charity_user.models import CharityUser
from message.models import Message


class MessageUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CharityUser
        fields = ["id", "name"]


class ViewMessageSerializer(serializers.ModelSerializer):
    message_user = MessageUserSerializer(read_only=True)

    class Meta:
        model = Message
        fields = ["id", "message", "message_user"]


class CreateMessageSerializer(serializers.ModelSerializer):
    message_user_id = serializers.IntegerField(required=True)

    class Meta:
        model = Message
        fields = ["id", "message", "message_user_id"]

    def create(self, validated_data):
        data = {k: v for k, v in validated_data.items() if k != "message_user_id"}

        message = Message(**data)
        message.charity_user = CharityUser.objects.get(
            pk=validated_data["message_user_id"]
        )
        message.save()
        return message
