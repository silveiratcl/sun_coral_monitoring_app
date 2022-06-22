from django.views.generic.base import TemplateView


class MarkerMapView(TemplateView):
    """Markers map view."""

    template_name = "map.html"