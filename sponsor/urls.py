from django.urls import path

from sponsor.views import SponsorCreateAPIView, SponsorDetailView, SponsorView


urlpatterns = [
    path("", SponsorView.as_view(), name="sponsors-api"),
    path("", SponsorCreateAPIView.as_view(), name="sponsor-create"),
    path("sponsor_detail/", SponsorDetailView.as_view(), name="sponsor-detail-api"),
]
