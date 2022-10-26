from django.db import connection
from django.contrib.auth.models import User
from django.http import HttpRequest
from django.test import TestCase, Client
from rest_framework import status
from model_bakery import baker
import datetime
import json
import unittest 

from api.application.api_service import ApiService
from api.infrastructure.api_view import ApiView
from api.infrastructure.models import Image


class ApiViewTest(TestCase):
    
    unittest.TestCase.maxDiff = None

    def setUp(self) -> None:
        self.api_service = ApiService(connection)
        self.api_view = ApiView(self.api_service)
        self.user = User.objects.create_user(username='tester', password='test1234', email='test@example.com')
        self.user.save()
        self.client = Client()
        self.client.login(username='tester', password='test1234')
        self.request = HttpRequest()

    def test_get_images_call(self) -> None:
        self.images = baker.make(Image, _quantity=30)
        request = self.request
        request.user = self.user
        response = self.api_view.get(request=request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_images_call_404(self) -> None:
        request = self.request
        request.user = self.user
        response = self.api_view.get(request=request)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_post_event_call(self) -> None:
        image = baker.make(Image)
        request = self.request
        request.user = self.user
        body = bytes(json.dumps({"eventType": "click", "timestamp": datetime.datetime.now().timestamp()}), encoding='utf-8')
        request._body = body
        imageId = image.id
        response = self.api_view.post(request=request, imageId=imageId)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_post_event_400_error_call(self) -> None:
        image = baker.make(Image)
        request = self.request
        request.user = self.user
        request._body = None
        response = self.api_view.post(request=request, imageId=image.id)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_post_event_404_error_call(self) -> None:
        request = self.request
        request.user = self.user
        body = bytes(json.dumps({"eventType": "click", "timestamp": datetime.datetime.now().timestamp()}), encoding='utf-8')
        request._body = body
        response = self.api_view.post(request=request, imageId=None)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)