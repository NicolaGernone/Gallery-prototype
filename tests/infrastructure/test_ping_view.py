from django.db import connection
from django.test import TestCase
from rest_framework import status

from api.application.ping_service import PingService
from api.infrastructure.ping_view import PingView


class PingViewTest(TestCase):

    def setUp(self):
        self.ping_service = PingService(connection)
        self.ping_view = PingView(self.ping_service)

    def test_get_ping(self):
        response = self.ping_view.get(request='')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
