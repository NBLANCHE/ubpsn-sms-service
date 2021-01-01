from rest_framework import serializers
from charity_user.models import CharityUser


class CharityUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CharityUser
        fields = ["id", "name", "phone_number", "subscribed_newsletter_topics"]
