from django.urls import path
from .views import SponsorApi

urlpatterns = [
    path('', SponsorApi.as_view(), name='sponsor-create')
]
