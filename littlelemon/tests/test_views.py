# In tests/test_views.py

from django.test import TestCase
from rest_framework.test import APIClient
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer

class MenuViewTest(TestCase):
    def setUp(self):
        # Set up test instances of the Menu model
        Menu.objects.create(title="Dish1", price=10, inventory=20)
        Menu.objects.create(title="Dish2", price=15, inventory=25)
        Menu.objects.create(title="Dish3", price=20, inventory=30)

    def test_getall(self):
        # Retrieve all Menu objects using the API client
        client = APIClient()
        response = client.get('/restaurant/menu/')  # Replace with your actual API endpoint

        # Check if the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Serialize the test instances and compare with the response data
        expected_data = MenuSerializer(Menu.objects.all(), many=True).data
        self.assertEqual(response.data, expected_data)
