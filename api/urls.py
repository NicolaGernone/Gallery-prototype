from django.urls import path
from api.infrastructure.api_view import ApiView
from django.views.generic import TemplateView

app_name = 'api'

urlpatterns = [
    path('', TemplateView.as_view(template_name="home.html"), name="home"),
    path('images', ApiView.as_view(), name="gallery"),
    path('images/<str:imageId>/events', ApiView.as_view())
]
