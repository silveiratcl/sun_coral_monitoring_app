"""Markers urls."""

from django.urls import path

from marker.views import MarkerMapView

app_name = "marker"

urlpatterns = [
    path("map/", MarkerMapView.as_view()),
]