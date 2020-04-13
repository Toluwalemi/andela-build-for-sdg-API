from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from rest_framework.response import Response

from api import serializers
from api.serializers import EstimatorSerializer
from api import estimator


class UserInputAPIView(generics.CreateAPIView):
    serializer_class = EstimatorSerializer

    # def list(self, request):
    #     serializer = serializers.EstimatorSerializer(
    #         instance=result.values(), many=True)
    #     return Response(serializer.data)
