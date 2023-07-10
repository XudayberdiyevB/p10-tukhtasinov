from django.urls import path
from sponsor.views import SponsorView

urlpatterns = [
    path('', SponsorView.as_view(), name='sponsors-api'),
]
