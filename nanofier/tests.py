from rest_framework.test import APITestCase
from rest_framework import status
from .models import NanoURL


class URLNanofierTests(APITestCase):
    def test_nanofy_returns_nano_url(self):
        """
        Ensure POST /nanofy/ returns a nano_url
        """

        response = self.client.post(
            "/nanofy/", {"original_url": "https://example.com/test"}, format="json"
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn("nano_url", response.data)
        self.assertIn("original_url", response.data)

    def test_resolve_fails_for_nonexistent_code(self):
        """
        Ensure /resolve/ returns 400 if nano code is invalid
        """

        fake_url = "http://localhost:8000/fake123/"
        response = self.client.post("/resolve/", {"nano_url": fake_url}, format="json")
        print(response.status_code)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("nano_url", response.data)
