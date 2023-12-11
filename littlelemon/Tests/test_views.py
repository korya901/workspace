# tests/test_views.py
from django.test import TestCase
from rest_framework.test import APIClient
from restaurant.models import Menu 
from restaurant.views import MenuItemView  

class MenuViewTest(TestCase):
    def setUp(self):
        # Create a few test instances of the Menu model
        Menu.objects.create(title='Dish1', price=9.99)
        Menu.objects.create(title='Dish2', price=14.99)

        # Set up the test client
        self.client = APIClient()

    def test_getall(self):
        # Retrieve all Menu objects
        response = self.client.get('/menus/')  # Adjust the URL as needed

        # Check if the request was successful (status code 200)
        self.assertEqual(response.status_code, 200)

        # Serialize the data
        serialized_data = MenuItemView.get_serializer(Menu.objects.all(), many=True).data

        # Check if the serialized data equals the response data
        self.assertEqual(response.data, serialized_data)
