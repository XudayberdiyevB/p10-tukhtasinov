from rest_framework import generics
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED
from rest_framework.views import APIView

from sponsor.models import Sponsor
from sponsor.serializers import SponsorDetailSerializers, SponsorListSerializer


class SponsorDetailView(generics.RetrieveAPIView):
    queryset = Sponsor.objects.all()
    serializer_class = SponsorDetailSerializers


class SponsorView(generics.ListAPIView):
    queryset = Sponsor.objects.order_by("-created_at")
    serializer_class = SponsorListSerializer


class SponsorCreateAPIView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = SponsorSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=HTTP_201_CREATED)
