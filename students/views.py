from datetime import datetime
from django.http import JsonResponse
from django.utils.dates import MONTHS
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.generics import ListCreateAPIView
from rest_framework.views import APIView
from rest_framework import generics
from paginations import CustomPageNumberPagination
from sponsors.models import Sponsor
from students.serializers import StudentListCreateSerializer, StudentDetailSerializer
from .models import Student


class StudentListCreateView(ListAPIView):
from students.serializers import StudentDetailSerializer, StudentSerializer

from .models import Student


class StudentsListView(ListCreateAPIView):
>>>>>>> students/views.py
    queryset = Student.objects.all()
    pagination_class = CustomPageNumberPagination

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return StudentListCreateSerializer
        return StudentListCreateSerializer


class StudentsAndSponsorsCountApi(APIView):
    def get(self, request):
        year = datetime.now().year
        result = {"sponsors": [], "students": []}

        for index, month in MONTHS.items():
            students = Student.objects.filter(created_at__year=year, created_at__month=index).count()
            sponsors = Sponsor.objects.filter(created_at__year=year, created_at__month=index).count()
            result.get("students").append({month: students if students > 0 else 0})
            result.get("sponsors").append({month: sponsors if students > 0 else 0})

        return JsonResponse(result)


<<<<<<< students/views.py
class StudentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    lookup_field = 'id'

    def get_serializer_class(self):
        if self.request.method in ["POST", "PATCH"]:
            return StudentDetailSerializer
        return StudentDetailSerializer
=======
class StudentListCreateView(generics.ListCreateAPIView):
    queryset = Student.objects.order_by("-id")
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_fields = ("degree", "university")
    ordering_fields = ("id", "full_name")
    search_fields = ("full_name", "university")
    pagination_class = CustomPageNumberPagination

    def get_serializer_class(self):
        if self.request.method == "POST":
            return StudentSerializer
        return StudentSerializer


class StudentDetailView(generics.RetrieveUpdateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentDetailSerializer
>>>>>>> students/views.py
