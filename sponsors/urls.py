from django.urls import path

from sponsors.views import (
    SponsorDetailView,
    SponsorListCreateView,
    SponsorMoneyDashboard,
    SponsorListForSelect,
)


urlpatterns = [
    path("", SponsorListCreateView.as_view(), name="sponsor_list_create"),
    path("<int:pk>/", SponsorDetailView.as_view(), name="sponsor_detail"),
    path("dashboard/", SponsorMoneyDashboard.as_view(), name="sponsors-dashboard"),
    path("sponsor_select/", SponsorListForSelect.as_view(), name="sponsor-list-select"),
]
