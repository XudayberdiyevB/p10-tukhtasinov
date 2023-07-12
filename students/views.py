from datetime import datetime
from django.http import JsonResponse
from django.utils.dates import MONTHS
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework import generics
from paginations import CustomPageNumberPagination
from sponsors.models import Sponsor
from students.serializers import StudentListCreateSerializer, StudentDetailSerializer
from .models import Student


class StudentListCreateView(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentListCreateSerializer
    pagination_class = CustomPageNumberPagination


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


class StudentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    lookup_field = 'id'

    def get_serializer_class(self):
        if self.request.method in ["POST", "PATCH"]:
            return StudentDetailSerializer
        return StudentDetailSerializer
