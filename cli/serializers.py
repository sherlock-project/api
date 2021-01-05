from django.contrib.auth.models import User, Group
from django.db import models
from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer):
    """
    TODO: We do not need this, this is only for testing purpose
    """
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']
