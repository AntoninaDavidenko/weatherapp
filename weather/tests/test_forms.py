from django.test import TestCase
from weather.forms import CityForm


class CityFormTestCase(TestCase):

    def test_empty_name_is_not_valid(self):
        form = CityForm({'name': ''})
        self.assertFalse(form.is_valid())
        print(form.is_valid())

    def test_name_is_valid(self):
        form = CityForm({'name': 'New York'})
        self.assertTrue(form.is_valid())
