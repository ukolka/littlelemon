from django.test import TestCase
from LittleLemonAPI import models

class MenuTest(TestCase):
    def test_get_item(self):
       item = models.MenuItem.objects.create(title='Icecream', price=80, inventory=100)
       self.assertEqual(str(item), "Icecream: 80")

