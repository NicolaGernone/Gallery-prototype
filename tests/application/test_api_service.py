from sqlite3 import DatabaseError
from django.db import connection
from django.contrib.auth.models import User
from django.http import HttpRequest
from django.test import TestCase, Client
from model_bakery import baker
import datetime
import json

from api.infrastructure.models import *

from api.application.api_service import ApiService


class ApiServiceTest(TestCase):

    def setUp(self):
        self.api_service = ApiService(connection)
        self.user = User.objects.create_user(username='tester', password='test1234', email='test@example.com')
        self.user.save()
        self.client = Client()
        self.client.login(username='tester', password='test1234')
        self.request = HttpRequest()

    def test_get_images(self):
        self.images = baker.make(Image, _quantity=3)
        self.event = baker.make(Event, image_id=self.images[0].id)

        self.list_of_images = [
            {"id": self.images[0].id, "name": self.images[0].name, "weight": None, "url": self.images[0].url, "categories": None, "events": { "view": None, "click": None}},
            {"id": self.images[1].id, "name": self.images[1].name, "weight": None, "url": self.images[1].url, "categories": None, "events": { "view": None, "click": None}},
            {"id": self.images[2].id, "name": self.images[2].name, "weight": None, "url": self.images[2].url, "categories": None, "events": { "view": None, "click": None}}
            ]

        dataSet = {'data': self.list_of_images}
        request = self.request
        request.user = self.user
        response = self.api_service.get_images(request)
        self.assertEqual(response, dataSet)

    def test_set_events(self):
        image = baker.make(Image)
        request = self.request
        request.user = self.user
        body = bytes(json.dumps({"eventType": "click", "timestamp": datetime.datetime.now().timestamp()}), encoding='utf-8')
        request._body = body
        imageId = image.id
        response = self.api_service.set_events(request=request, imageId=imageId)
        self.assertEqual(response, {})

    def test_get_images(self):

        request = self.request
        request.user = self.user
        with self.assertRaises(DatabaseError):
            self.api_service.get_images(request)

    def test_set_events_fail(self):
        request = self.request
        request.user = self.user
        body = bytes(json.dumps({ "eventType": "click", "timestamp": datetime.datetime.now().timestamp()}), encoding='utf-8')
        request._body = body
        imageId = None
        with self.assertRaises(DatabaseError):
            self.api_service.set_events(request=request, imageId=imageId)
        