from datetime import datetime

from django.http import JsonResponse
from rest_framework.generics import ListAPIView

from paginations import CustomPageNumberPagination
from student.models import Student
from student.serializers import StudentSerializer
from sponsor.models import Sponsor
from sponsor.serializers import SponsorListSerializer
from .models import Student
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED
from django.utils.dates import MONTHS


class StudentView(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    pagination_class = CustomPageNumberPagination


class StudentsAndSponsorsCountApi(APIView):
    def get(self, request):
        year = datetime.now().year
        result = {
            "sponsors": [],
            "students": []
        }
        
        for index, month in MONTHS.items():
            students = Student.objects.filter(created_at__year=year,
                                              created_at__month=index).count()
            sponsors = Sponsor.objects.filter(created_at__year=year,
                                              created_at__month=index).count()
            result.get('students').append({
                month: students if students > 0 else 0
            })
            result.get('sponsors').append({
                month: sponsors if students > 0 else 0
            })
        
        return JsonResponse(result)
