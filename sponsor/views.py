from django.db.models import Sum
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED
from rest_framework.views import APIView

from sponsor.models import Sponsor
from sponsor.serializers import SponsorDetailSerializers, SponsorListSerializer, SponsorCreateSerializer
from student.models import StudentSponsor, Student


class SponsorDetailView(generics.RetrieveAPIView):
    queryset = Sponsor.objects.all()
    serializer_class = SponsorDetailSerializers


class SponsorView(generics.ListAPIView):
    queryset = Sponsor.objects.order_by("-created_at")
    serializer_class = SponsorListSerializer


class SponsorCreateAPIView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = SponsorCreateSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=HTTP_201_CREATED)


class SponsorMoneyDashboard(APIView):
    def get(self, request, *args, **kwargs):
        paid_amount = StudentSponsor.objects.aggregate(paid_amount=Sum('amount')).get('paid_amount') or 0
        requested_amount = Student.objects.aggregate(requested_amount=Sum('tuition_fee')).get('requested_amount') or 0
        amount_tobe_paid = requested_amount - paid_amount
        data = {
            'paid_amount': paid_amount,
            'requested_amount': requested_amount,
            'amount_tobe_paid': amount_tobe_paid
        }

        return Response(data)
