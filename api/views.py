# Create your views here.
from rest_framework import generics
from rest_framework.renderers import JSONRenderer
from rest_framework.views import APIView
from rest_framework_xml.parsers import XMLParser
from rest_framework_xml.renderers import XMLRenderer

from api.serializers import EstimatorSerializer


class UserInputAPIView(generics.CreateAPIView):
    serializer_class = EstimatorSerializer

    # def list(self, request):
    #     serializer = serializers.EstimatorSerializer(
    #         instance=result.values(), many=True)
    #     return Response(serializer.data)


class JsonAPIView(APIView):
    renderer_classes = [JSONRenderer]


class XmlAPIView(APIView):
    renderer_classes = (XMLRenderer,)
    parser_classes = (XMLParser,)


class LogsAPIView(generics.ListAPIView):
    pass
