from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from cli.serializers import UserSerializer

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.

    TODO: We do not need this, this is only for testing purpose
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

class MyOwnView(APIView):
    def get(self, request):
        return Response({'some': 'data'})

@api_view(['GET'])
def hello_world(request):
    return Response({"message": "Hello, world!"})
