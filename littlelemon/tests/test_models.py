from django.test import TestCase
from restaurant.models import Menu, Booking
from decimal import Decimal
from datetime import datetime


class MenuTest(TestCase):
    def test_create_item(self):
        item = Menu.objects.create(name="IceCream", price=Decimal('80'))
        self.assertEqual(str(item), "IceCream")


class BookingTest(TestCase):
    def test_create_booking(self):
        booking = Booking.objects.create(
            first_name="John Doe",
            reservation_slot=4,
            reservation_date=datetime(2023, 6, 24, 18, 0)
        )
        expected_str = "John Doe"
        self.assertEqual(str(booking), expected_str)