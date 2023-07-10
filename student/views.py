from rest_framework.generics import ListAPIView

from paginations import CustomPageNumberPagination
from student.models import Student
from student.serializers import StudentSerializer


class StudentView(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    pagination_class = CustomPageNumberPagination
