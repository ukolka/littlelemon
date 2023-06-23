from rest_framework.serializers import ModelSerializer
from restaurant import models

class MenuItemSerializer(ModelSerializer):
    class Meta():
        model = models.Menu 
        fields = ['id', 'title', 'price', 'inventory']
