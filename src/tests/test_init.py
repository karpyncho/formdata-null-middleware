from http import HTTPStatus

from django.test import TestCase
from django.urls import reverse


class TestInit(TestCase):
    def test_middleware(self):
        response = self.client.get(reverse("hello"))
        self.assertEqual(HTTPStatus.OK, response.status_code)
