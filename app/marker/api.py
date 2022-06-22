"""Marker API URL Configuration."""

from rest_framework import routers

from marker.viewsets import MarkerViewSet

router = routers.DefaultRouter()
router.register(r"marker", MarkerViewSet)

urlpatterns = router.urls