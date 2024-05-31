import uuid
from django.test import TestCase, Client
from weather.models import City
from django.urls import reverse


class DeleteCityTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_delete_city_with_uuid(self):
        city_uuid = uuid.uuid4()
        city = City.objects.create(
            id=city_uuid,
            name="London",
        )

        response = self.client.get(reverse('delete', args=[city.id]))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(City.objects.filter(id=city.id).count(), 0)
        self.assertRedirects(response, reverse('home'))


class ErrorHandlingTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_invalid_city_name(self):
        response = self.client.post('/home', {'name': 'Lviiv'})
        self.assertContains(response, 'Oops! Please write correct city name')
