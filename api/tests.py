from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient


class WeatherAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_get_weather(self):
        response = self.client.get(
            reverse("weather_api", kwargs={"location": "nairobi", "days": 3})
        )
        self.assertEqual(response.status_code, 200)
        self.assertIn("maximum", response.data)
        self.assertIn("minimum", response.data)
        self.assertIn("average", response.data)

    def test_get_weather_with_invalid_location(self):
        response = self.client.get(
            reverse("weather_api", kwargs={"location": "mordor", "days": 3})
        )
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.data["error"], "Something went wrong")

    def test_get_weather_with_invalid_days(self):
        response = self.client.get(
            reverse("weather_api", kwargs={"location": "nairobi", "days": 15})
        )
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.data["error"], "Error: list index out of range")

    def test_get_weather_with_invalid_location_and_days(self):
        response = self.client.get(
            reverse("weather_api", kwargs={"location": "mordor", "days": 18})
        )
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.data["error"], "Something went wrong")

    def test_get_weather_with_invalid_location_and_valid_days(self):
        response = self.client.get(
            reverse("weather_api", kwargs={"location": "mordor", "days": 3})
        )
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.data["error"], "Something went wrong")

    def test_get_weather_with_valid_location_and_invalid_days(self):
        response = self.client.get(
            reverse("weather_api", kwargs={"location": "nairobi", "days": 30})
        )
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.data["error"], "Something went wrong")

    def test_get_weather_with_invalid_location_and_invalid_days(self):
        response = self.client.get(
            reverse("weather_api", kwargs={"location": "mordor", "days": 150})
        )
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.data["error"], "Something went wrong")
