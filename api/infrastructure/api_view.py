from django.db import DatabaseError

from api.application.api_service import ApiService
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.db import connection
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import render
from django.views import View
from rest_framework import status


class ApiView(View):

    def __init__(self, api_service=ApiService(connection)):
        self.service = api_service
    
    user = get_user_model()
    
    @login_required
    def get(self, request: HttpRequest) -> HttpResponse:
        template = "gallery.html"
        try:
            context = self.service.get_images(request)
            return render(request, template, context, status=status.HTTP_200_OK)
        except DatabaseError as e:
            context = { 'error' : str(e) }
            return render(request, template, context, status=status.HTTP_404_NOT_FOUND)

    def post(self, request: HttpRequest, imageId: str) -> JsonResponse:
        if request.body:
            try:
                return JsonResponse(self.service.set_events(request, imageId), status=status.HTTP_204_NO_CONTENT)
            except DatabaseError:
                return JsonResponse({ 'error' : "There are no image with the specified ID." }, status=status.HTTP_404_NOT_FOUND)
        else:
            return JsonResponse({ 'error' : "There was an error parsing the given request" }, status=status.HTTP_400_BAD_REQUEST)

                