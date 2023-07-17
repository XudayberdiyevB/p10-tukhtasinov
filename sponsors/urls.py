from django.urls import path

from sponsors.views import (
    SponsorListCreateView,
    SponsorMoneyDashboard,
    SponsorListForSelect,
    SponsorRetrieveUpdateDestroyAPIView,
)


urlpatterns = [
    path("", SponsorListCreateView.as_view(), name="sponsor_list_create"),
    path("<int:pk>/", SponsorRetrieveUpdateDestroyAPIView.as_view(), name="sponsor-detail-edit-delete"),
    path("dashboard/", SponsorMoneyDashboard.as_view(), name="sponsors-dashboard"),
    path("sponsors-for-select/", SponsorListForSelect.as_view(), name="sponsors-list-select"),
]
