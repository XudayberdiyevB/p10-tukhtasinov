from django.urls import path

from sponsor.views import SponsorListCreateView, SponsorDetailView, SponsorMoneyDashboard

urlpatterns = [
    path('', SponsorListCreateView.as_view(), name='sponsor_list_create'),
    path('<int:pk>/', SponsorDetailView.as_view(), name='sponsor_detail'),
    path('dashboard/', SponsorMoneyDashboard.as_view(), name="sponsor-dashboard")
]
