from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView
from rest_framework.generics import RetrieveUpdateAPIView, DestroyAPIView
from rest_framework.viewsets import ModelViewSet
from restaurant import models
from restaurant import serializers
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication



# Create your views here.
def index(request):
    return render(request, 'index.html')

class MenuItemView(ListCreateAPIView):
    queryset = models.Menu.objects.all()
    serializer_class = serializers.MenuItemSerializer

class SingleMenuItemView(RetrieveUpdateAPIView, DestroyAPIView):
    queryset = models.Menu.objects.all()
    serializer_class = serializers.MenuItemSerializer

class BookingViewSet(ModelViewSet):
    queryset = models.Booking.objects.all()
    serializer_class = serializers.BookingSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
