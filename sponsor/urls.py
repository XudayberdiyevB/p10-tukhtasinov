from django.urls import path
from sponsor.views import SponsorView, SponsorCreateAPIView

urlpatterns = [
    path("", SponsorView.as_view(), name='sponsors-api'),
    path("", SponsorCreateAPIView.as_view(), name="sponsor-create")
]
