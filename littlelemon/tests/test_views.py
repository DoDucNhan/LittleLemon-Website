from django.test import TestCase
from restaurant.models import Menu


class MenuItemsViews(TestCase):
    def setUp(self):
        shakshuka = Menu.objects.create(name='shakshuka', price=8.50)
        Hummus = Menu.objects.create(name='Hummus', price=5.00)
    
    def test_menu_items_list(self):
        response = self.client.get('/menu/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'shakshuka')
        self.assertContains(response, 'Hummus')