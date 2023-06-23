from rest_framework.serializers import ModelSerializer
from LittleLemonAPI import models

class MenuItemSerializer(ModelSerializer):
    class Meta:
        model = models.MenuItem
        fields = ['id', 'title', 'price', 'inventory']

