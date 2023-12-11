# tests/test_models.py

from django.test import TestCase
from restaurant.models import Menu 

class MenuTest(TestCase):
    def get_test_item(self):
        # Create a Menu instance
        item = Menu.objects.create(title="IceCream", price=80, inventory=100)
        self.assertEqual(item, "IceCream : 80")
        
        # Compare the string representation with the expected value
        expected_str = 'Test Dish : 10.99'
        self.assertEqual(str(Menu), expected_str)
