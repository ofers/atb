from django.contrib.auth.models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'pid', 'department']

# class ContactSerializer(serializers.ModelSerializer):
#     name = serializers.CharField(required=True)
#     slack = Base64JsonField(required=False)
#     email = Base64JsonField(required=False)
#     webhook = Base64JsonField(required=False)