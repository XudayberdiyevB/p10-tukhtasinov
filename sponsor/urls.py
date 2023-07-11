from django.urls import path

from sponsor.views import SponsorCreateAPIView, SponsorDetailView, SponsorView, SponsorMoneyDashboard

urlpatterns = [
    path("", SponsorView.as_view(), name="sponsors-api"),
    path("create/", SponsorCreateAPIView.as_view(), name="sponsor-create"),
    path("detail/", SponsorDetailView.as_view(), name="sponsor-detail-api"),
    path('dashboard/', SponsorMoneyDashboard.as_view(), name="sponsor-dashboard")
]
