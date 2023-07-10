from rest_framework import generics
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

