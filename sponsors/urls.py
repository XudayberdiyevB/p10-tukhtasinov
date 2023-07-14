from django.urls import path

from sponsors.views import (
    SponsorListCreateView,
    SponsorMoneyDashboard,
    SponsorRetrieveUpdateDestroyAPIView,
)


urlpatterns = [
    path("", SponsorListCreateView.as_view(), name="sponsor_list_create"),
    path("<int:pk>/", SponsorRetrieveUpdateDestroyAPIView.as_view(), name="sponsor-detail-edit-delete"),
    path("dashboard/", SponsorMoneyDashboard.as_view(), name="sponsors-dashboard"),
]
