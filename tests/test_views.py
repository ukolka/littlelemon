from django.test import TransactionTestCase
from datetime import datetime
import json
from LittleLemonAPI import models
from restaurant.models import Booking
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token


class MenuViewTest(TransactionTestCase):
    reset_sequences = True

    def setUp(self):
        self.menu1 =  models.MenuItem.objects.create(
            title='Icecream', price=80, inventory=100)
        self.menu2 =  models.MenuItem.objects.create(
            title='Bubble Gum', price=40, inventory=1000)
        self.menu2 =  models.MenuItem.objects.create(
            title='Hamburger', price=60, inventory=200)
        self.user = User.objects.create_user(username='test_user', password='123qwe')
        token = str(Token.objects.create(user=self.user)) 
        self.request_headers = {'AUTHORIZATION': 'Token ' + token}

    def get(self, path):
        return self.client.get(path, headers=self.request_headers)

    def delete(self, path):
        return self.client.delete(path, headers=self.request_headers)

    def post(self, path, data):
        return self.client.post(
            path, 
            data,
            headers=self.request_headers,
        )

    def test_get_all(self):
        resp = self.get('/api/menu-items/')

        expected_serialized_data = b'[{"id":1,"title":"Icecream","price":"80.00","inventory":100},{"id":2,"title":"Bubble Gum","price":"40.00","inventory":1000},{"id":3,"title":"Hamburger","price":"60.00","inventory":200}]'

        self.assertEqual(resp.content, expected_serialized_data)

    def test_booking_main(self):
        resp = self.get('/api/booking/')

        self.assertEqual(resp.content, b'{"tables":"http://testserver/api/booking/tables/"}')
            
    def test_booking_tables_add(self):
        resp = self.get('/api/booking/tables/')

        self.assertEqual(resp.content, b'[]')

        resp = self.post('/api/booking/tables/', data={
            'name': 'Test Booking',
            'no_of_guests': 4,
            'booking_date': '2023-06-25T00:00:00'
        })

        self.assertEqual(resp.status_code, 201)
        self.assertEqual(
            resp.content[:72],
            ('{{"name":"Test Booking","no_of_guests":4,"booking_date":"{}"}}'.format(datetime.now().isoformat()).encode()[:72])
        )

        self.assertEqual(Booking.objects.count(), 1)

        resp = self.get('/api/booking/tables/1/')
        self.assertEquals(json.loads(resp.content)['name'], 'Test Booking')

    def test_menu_del(self):
        resp = self.get('/api/menu-items/1/')
        self.assertEquals(resp.status_code, 200)

        resp = self.delete('/api/menu-items/1/')
        self.assertEquals(resp.status_code, 204)

        resp = self.get('/api/menu-items/1/')
        self.assertEquals(resp.status_code, 404)
