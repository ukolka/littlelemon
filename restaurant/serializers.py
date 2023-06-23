from rest_framework.serializers import ModelSerializer
from restaurant import models

class MenuItemSerializer(ModelSerializer):
    class Meta():
        model = models.Menu 
        fields = ['id', 'title', 'price', 'inventory']


class BookingSerializer(ModelSerializer):
    class Meta():
        model = models.Booking
        fields = ['id', 'name', 'no_of_guests', 'booking_date']
