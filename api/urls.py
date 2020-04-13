from django.contrib import admin
from django.urls import path

from api.views import UserInputAPIView

urlpatterns = [
    path('', UserInputAPIView.as_view()),
]
