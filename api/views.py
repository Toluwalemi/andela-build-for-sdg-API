# Create your views here.
from rest_framework import generics, status
from rest_framework.generics import CreateAPIView
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer, BrowsableAPIRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_xml.parsers import XMLParser
from rest_framework_xml.renderers import XMLRenderer

from api.serializers import EstimatorSerializer


class UserInputAPIView(APIView):
    serializer_class = EstimatorSerializer

    def get(self, request, format=None):
        # estimators = Estimator
        serializer = EstimatorSerializer()
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = EstimatorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class JsonAPIView(APIView):
    renderer_classes = [JSONRenderer]

    def get(self, request, format=None):
        serializer = EstimatorSerializer(many=True)
        return Response(serializer.data)


class XmlAPIView(APIView):
    renderer_classes = (XMLRenderer,)
    parser_classes = (XMLParser,)

    def get(self, request, format=None):
        serializer = EstimatorSerializer(many=True)
        return Response(serializer.data)


class LogsAPIView(generics.ListAPIView):
    pass
