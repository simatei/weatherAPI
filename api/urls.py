from django.urls import path
from .views import WeatherAPIMainView

urlpatterns = [
    path(
        "locations/<str:location>/days=<int:days>/",
        WeatherAPIMainView.as_view(),
        name="weather_api",
    ),
]
