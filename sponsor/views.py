from rest_framework import generics
from rest_framework.filters import OrderingFilter, SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from paginations import CustomPageNumberPagination
from sponsor.models import Sponsor
from sponsor.serializers import SponsorListSerializer, SponsorCreateSerializer, SponsorDetailSerializer


class SponsorListCreateView(generics.ListCreateAPIView):
    queryset = Sponsor.objects.order_by("-created_at")
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_fields = ("full_name", "phone", "organization_name")
    ordering_fields = ("id", "full_name", 'created_at')
    search_fields = ("full_name", "created_at", "phone", 'organization_at')
    pagination_class = CustomPageNumberPagination

    def __str__(self):
        return self.full_name

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
