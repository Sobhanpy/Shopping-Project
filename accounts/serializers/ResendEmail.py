from accounts.models import CustomUser
from django.shortcuts import get_object_or_404
from rest_framework import serializers
 
class ResendEmailSerializer(serializers.Serializer):
    email = serializers.CharField(label=("Email"), write_only=True)

    def validate(self, attrs):
        user = get_object_or_404(CustomUser, email=attrs.get("email"))
        attrs["user"] = user
        return attrs