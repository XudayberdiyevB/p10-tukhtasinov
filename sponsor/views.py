from rest_framework import generics
from models import Sponsor
from serializers import SponsorDetailSerializers


class SponsorDetailView(generics.RetrieveAPIView):
    queryset = Sponsor.objects.all()
    serializer_class = SponsorDetailSerializers
