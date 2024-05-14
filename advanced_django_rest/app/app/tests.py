from django.test import SimpleTestCase
from app import calc
from rest_framework.test import APIClient

class CalcTests(SimpleTestCase):
    def test_add(self):
        self.assertEqual(calc.add(3, 8), 11)

    def test_get_greetings(self):
        client = APIClient()
        response = client.get('/healthcheck',  follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content.decode('utf-8'), 'ok')