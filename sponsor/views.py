from rest_framework import generics

from sponsor.models import Sponsor
from sponsor.serializers import SponsorSerializer


class SponsorView(generics.ListAPIView):
    queryset = Sponsor.objects.order_by("-created_at")
    serializer_class = SponsorSerializer