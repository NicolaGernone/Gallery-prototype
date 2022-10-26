from django.db import connection
from django.views import View
from rest_framework import status
from django.http import JsonResponse

from api.application.ping_service import PingService


class PingView(View):

    def __init__(self, ping_service=PingService(connection)):
        self.service = ping_service

    def get(self, request, *args, **kwargs):
        return JsonResponse(self.service.ping(), status=status.HTTP_200_OK)
