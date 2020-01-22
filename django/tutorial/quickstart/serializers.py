from django.contrib.auth.models import User
from rest_framework import serializers



class UserSerializer(serializers.ModelSerializer):
    # first_name = serializers.SerializerMethodField()
    # last_name = serializers.SerializerMethodField()
    # pid = serializers.SerializerMethodField()
    # department = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['first_name', 'last_name', ]
