import requests
from statistics import mean, median
from rest_framework import views, status
from rest_framework.response import Response
import environ

env = environ.Env()


class WeatherAPIMainView(views.APIView):
    def get(self, request, location, days):

        try:
            api_key = env("WEATHER_API_KEY")
            response = requests.get(
                f"http://api.weatherapi.com/v1/forecast.json?key={api_key}&q={location}&days={days}&aqi=no&alerts=no"
            )

            if response.status_code == 200:
                response = response.json()
                overall_day_stats = [
                    response["forecast"]["forecastday"][val]["day"]
                    for val in range(days)
                ]

                hourly_stats = [
                    response["forecast"]["forecastday"][val]["hour"]
                    for val in range(days)
                ]

                data = {
                    "maximum": max([val["maxtemp_c"] for val in overall_day_stats]),
                    "minimum": max([val["mintemp_c"] for val in overall_day_stats]),
                    "average": mean([val["avgtemp_c"] for val in overall_day_stats]),
                    "median": median(
                        [
                            val["temp_c"]
                            for val in [
                                hourly_stats[val][hour]
                                for val in range(days)
                                for hour in range(24)
                            ]
                        ]
                    ),
                }

                return Response(data, status=status.HTTP_200_OK)

            else:
                return Response(
                    {"error": "Something went wrong"},
                    status=status.HTTP_400_BAD_REQUEST,
                )

        except Exception as err:
            return Response(
                f"Error: {str(err)}",
                status=status.HTTP_400_BAD_REQUEST,
            )
