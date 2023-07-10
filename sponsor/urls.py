from django.urls import path

from .views import SponsorCreateAPIView


urlpatterns = [path("", SponsorCreateAPIView.as_view(), name="sponsor-create")]
