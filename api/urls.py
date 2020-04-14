from django.contrib import admin
from django.urls import path

from api.views import UserInputAPIView, JsonAPIView, XmlAPIView, LogsAPIView

urlpatterns = [
    path('', UserInputAPIView.as_view()),
    path('json/', JsonAPIView.as_view()),
    path('xml/', XmlAPIView.as_view()),
    path('logs/', LogsAPIView.as_view()),
]
