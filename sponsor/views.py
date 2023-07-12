from django.db.models import Sum
from rest_framework import generics
from rest_framework.filters import OrderingFilter, SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from paginations import CustomPageNumberPagination

from sponsor.models import Sponsor
from sponsor.serializers import SponsorDetailSerializers, SponsorListSerializer, SponsorCreateSerializer
from student.models import StudentSponsor, Student


class SponsorListCreateView(generics.ListCreateAPIView):
    queryset = Sponsor.objects.order_by("-created_at")
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_fields = ("full_name", "phone", "organization_name")
    ordering_fields = ("id", "full_name", 'created_at')
    search_fields = ("full_name", "created_at", "phone", 'organization_at')
    pagination_class = CustomPageNumberPagination

    def get_serializer_class(self):
        if self.request.method == "POST":
            return SponsorCreateSerializer
        return SponsorListSerializer


class SponsorDetailView(generics.RetrieveAPIView):
    queryset = Sponsor.objects.all()
    serializer_class = SponsorDetailSerializers


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
