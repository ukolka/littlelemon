from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView
from rest_framework.generics import RetrieveUpdateAPIView, DestroyAPIView
from restaurant import models
from restaurant import serializers

# Create your views here.
def index(request):
    return render(request, 'index.html')

class MenuItemView(ListCreateAPIView):
    queryset = models.Menu.objects.all()
    serializer_class = serializers.MenuItemSerializer

class SingleMenuItemView(RetrieveUpdateAPIView, DestroyAPIView):
    queryset = models.Menu.objects.all()
    serializer_class = serializers.MenuItemSerializer

