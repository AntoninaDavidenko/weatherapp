from django.test import TestCase
from weather.models import City


class CityModelTestCase(TestCase):

    def test_create_city(self):
        city = City(name="New York")
        self.assertEqual(city.name, "New York")

    def test_max_length(self):
        city = City(name="New York")
        max_length = city._meta.get_field('name').max_length
        self.assertEqual(max_length, 30)
