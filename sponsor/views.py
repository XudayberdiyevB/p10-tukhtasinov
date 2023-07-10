from rest_framework import generics
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED
from rest_framework.views import APIView

from sponsor.models import Sponsor
from sponsor.serializers import SponsorListSerializer, SponsorCreateSerializer, SponsorDetailSerializer


class SponsorListCreateView(generics.ListCreateAPIView):
    queryset = Sponsor.objects.order_by("-created_at")

    def get_serializer_class(self):
        if self.request.method == "POST":
            return SponsorCreateSerializer
        return SponsorListSerializer


class SponsorDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Sponsor.objects.order_by("-created_at")

    def get_serializer_class(self):
        if self.request.method in ['POST', 'PATCH']:
            return SponsorDetailSerializer
        return SponsorDetailSerializer

