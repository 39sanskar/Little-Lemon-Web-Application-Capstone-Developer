from django.test import TestCase
from restaurant.models import Menu, Booking

class MenuTestCase(TestCase):
    def instance(self):
        item = Menu.objects.create(title="IceCream", price=80, inventory=100)
        self.assertEqual(item, "IceCream : 80")

class MenuViewTest(TestCase):
    def test_get_all(self):
        Menu.objects.create(title="IceCream", price=80, inventory=100)
        items = Menu.objects.all()
        self.assertEqual(len(items), 1)
