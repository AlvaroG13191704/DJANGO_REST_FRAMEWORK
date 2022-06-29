
from rest_framework import serializers

class loginSocialSerializer(serializers.Serializer):
    token_id = serializers.CharField(required=True)