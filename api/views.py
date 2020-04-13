# Create your views here.
from rest_framework import generics

from api.serializers import EstimatorSerializer


class UserInputAPIView(generics.CreateAPIView):
    serializer_class = EstimatorSerializer

    # def list(self, request):
    #     serializer = serializers.EstimatorSerializer(
    #         instance=result.values(), many=True)
    #     return Response(serializer.data)
