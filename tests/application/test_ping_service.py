from django.db import connection
from django.test import TestCase

from api.application.ping_service import PingService


class PingServiceTest(TestCase):

    def setUp(self):
        self.ping_service = PingService(connection)

    def test_get_ping(self):
        response = self.ping_service.ping()
        self.assertEqual(response, {'message': 'pong'})
