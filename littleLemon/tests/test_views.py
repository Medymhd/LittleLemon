from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from restaurant.models import MenuItem
from restaurant.serializers import MenuItemSerializer
from django.urls import reverse


class MenuviewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        
        MenuItem.objects.create(Title= 'Burger', Price = 75.00, Inventory = 100)
        MenuItem.objects.create(Title= 'Sushi', Price = 80.00, Inventory = 25)
        MenuItem.objects.create(Title='Fries', Price=5.0, Inventory=5)
        
        user = User.objects.create_user(username = 'testuser' , password = 'pass')
        self.client.force_authenticate(user=user)
        
    def test_getall(self):
        response = self.client.get(reverse('menu-items'))
        MenuItems = MenuItem.objects.all()
        serializer = MenuItemSerializer(MenuItems, many=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, serializer.data)
        