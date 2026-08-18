from django.test import TestCase
from rest_framework.test import APIClient

from .models import Menu


class MenuAPITestCase(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.menu = Menu.objects.create(
            Title="Biryani",
            Price=120.00,
            Inventory=5
        )

    def test_get_menu_items(self):
        response = self.client.get("/restaurant/menu/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)

    def test_create_menu_item(self):
        response = self.client.post(
            "/restaurant/menu/",
            {
                "Title": "Pasta",
                "Price": "150.00",
                "Inventory": 10
            },
            format="json"
        )

        self.assertEqual(response.status_code, 201)
        self.assertEqual(Menu.objects.count(), 2)