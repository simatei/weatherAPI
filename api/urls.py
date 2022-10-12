from django.urls import path
from .views import WeatherAPIMainView

urlpatterns = [path("weather/", WeatherAPIMainView.as_view(), name="main-api-view")]
