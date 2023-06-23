from rest_framework.generics import ListCreateAPIView
from rest_framework.generics import RetrieveUpdateAPIView, DestroyAPIView 
from django.shortcuts import render
from rest_framework import response
from . import models
from . import serializers

from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication


@api_view()
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
def msg(request):
    return response.Response({"message":"This view is protected"})

# Create your views here.
class MenuItemView(ListCreateAPIView):
    queryset = models.MenuItem.objects.all()
    serializer_class = serializers.MenuItemSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

class SingleMenuItemView(RetrieveUpdateAPIView, DestroyAPIView):
    queryset = models.MenuItem.objects.all()
    serializer_class = serializers.MenuItemSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
