from django.test import TestCase
from rest_framework import status
import requests


class APITest(TestCase):

    def setUp(self):
        self.weather_url = 'http://127.0.0.1:8000/apis/weather'
        self.min_avg_url = 'http://127.0.0.1:8000/apis/stats/min_avg'
        self.max_avg_url = 'http://127.0.0.1:8000/apis/stats/max_avg'

    def test_weather_api_with_no_param_then_ok(self):
        response = requests.get(self.weather_url)
        self.assertEqual(response.status_code, 200)

    def test_weather_api_with_all_param_then_ok(self):
        response = requests.get(self.weather_url, {'location': 'USC00110072', 'year': '1985', 'page': 100})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_stats_min_avg_api_with_no_param_then_bad_request(self):
        response = requests.get(self.min_avg_url)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_stats_max_avg_api_with_no_param_then_bad_request(self):
        response = requests.get(self.max_avg_url)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_stats_min_avg_api_with_param_then_ok(self):
        response = requests.get(self.min_avg_url, {'location': 'USC00110072', 'year': '1985'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(response.text.__contains__('-1.1918'))

    def test_stats_max_avg_api_with_param_then_ok(self):
        response = requests.get(self.max_avg_url, {'location': 'USC00110072', 'year': '1985'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(response.text.__contains__('15.3205'))
