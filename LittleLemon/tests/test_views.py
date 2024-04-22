from django.test import TestCase
from rest_framework.test import APIClient
from restaurant import models
from restaurant import serializers


class MenuViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.menu_item1 = models.MenuItem.objects.create(title="Burger", price=10.99, inventory=50)
        self.menu_item2 = models.MenuItem.objects.create(title="Pizza", price=12.99, inventory=40)

    def test_getall(self):
        response = self.client.get('/restaurant/menu/items/')
        menu_items = models.MenuItem.objects.all()
        serializer = serializers.MenuSerializer(menu_items, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, 200)