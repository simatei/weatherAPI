import requests
from rest_framework import views, status
from rest_framework.response import Response


class WeatherAPIMainView(views.APIView):
    def get(self, request):
        return Response("OK") 