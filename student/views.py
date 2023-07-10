from rest_framework.generics import ListAPIView

from student.serializers import StudentSerializer
from paginators import CustomPageNumberPagination
from student.models import Student


class StudentView(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    pagination_class = CustomPageNumberPagination