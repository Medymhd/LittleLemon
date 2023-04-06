from django.test import TestCase
from restaurant.models import MenuItem

class MenuItemTest(TestCase):
    def test_get_item(self):
        item = MenuItem.objects.create(Title = "Strawberry IceCream", Price=8.00, Inventory = 100)
        itemstr= item.get_item()
        self.assertEqual(itemstr, "Strawberry IceCream : 8.00")
        