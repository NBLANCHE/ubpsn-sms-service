from rest_framework import serializers

from charity_user.models import CharityUser
from message.models import Message, IncomingSms


class MessageUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CharityUser
        fields = ["id", "name"]


class ViewMessageSerializer(serializers.ModelSerializer):
    message_user = MessageUserSerializer(read_only=True)
    message_status = serializers.CharField(read_only=True)

    class Meta:
        model = Message
        fields = ["id", "message", "message_status", "message_user"]


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
        return message


class SmsRequestSerializer(serializers.Serializer):
    MessageSid = serializers.CharField(max_length=34, required=True, source="sms_sid")
    AccountSid = serializers.CharField(
        max_length=34, required=True, source="account_sid"
    )
    From = serializers.CharField(max_length=30, required=True, source="from_number")
    To = serializers.CharField(max_length=30, required=True, source="to_number")
    Body = serializers.CharField(max_length=160, required=True, source="body")
    FromCity = serializers.CharField(max_length=100, required=False, source="from_city")
    FromState = serializers.CharField(
        max_length=100, required=False, source="from_state"
    )
    FromCountry = serializers.CharField(
        max_length=120, required=False, source="from_country"
    )

    def create(self, validated_data):
        return IncomingSms(**validated_data)
