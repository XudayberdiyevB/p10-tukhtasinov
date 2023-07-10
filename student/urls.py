from django.urls import path

from student.views import StudentView


app_name = 'student'

urlpatterns = [
    path('students/', StudentView.as_view(), name='students_list')
]