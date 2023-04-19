from django.test import TestCase
from rest_framework import status
import requests


class APITest(TestCase):

    def setUp(self):
        self.weather_url = 'http://127.0.0.1:8000/apis/weather'
        self.stats_url = 'http://127.0.0.1:8000/apis/weather/stats'

    def test_weather_api_with_no_param_then_ok(self):
        response = requests.get(self.weather_url)
        self.assertEqual(response.status_code, 200)

    def test_weather_api_with_all_param_then_ok(self):
        response = requests.get(self.weather_url, {'location': 'USC00110072', 'year': '1985', 'page': 100})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_weather_stats_api_with_no_param_then_ok(self):
        response = requests.get(self.stats_url)
        self.assertEqual(response.status_code, 200)

    def test_weather_stats_api_with_all_param_then_ok(self):
        response = requests.get(self.stats_url, {'location': 'USC00110072', 'year': '1985'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

