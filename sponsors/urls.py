from django.urls import path

from sponsors.views import (
    SponsorDetailView,
    SponsorListCreateView,
    SponsorMoneyDashboard,
    SponsorUpdateView,
)


urlpatterns = [
    path("", SponsorListCreateView.as_view(), name="sponsor_list_create"),
    path("<int:pk>/", SponsorDetailView.as_view(), name="sponsor_detail"),
    path("<int:pk>/edit/", SponsorUpdateView.as_view(), name="sponsor_edit"),
    path("dashboard/", SponsorMoneyDashboard.as_view(), name="sponsors-dashboard"),
]
