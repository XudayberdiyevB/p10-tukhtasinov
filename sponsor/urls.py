from django.urls import path

from sponsor.views import SponsorDetailView


urlpatterns = [
    path("sponsor_detail/", SponsorDetailView.as_view(), name="sponsor-detail-api"),
]
