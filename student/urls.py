from django.urls import path

from student.views import StudentView, StudentsAndSponsorsCountApi

app_name = "student"

urlpatterns = [
    path("", StudentView.as_view(), name="students_list"),
    path("student_sponsor_count", StudentsAndSponsorsCountApi.as_view(), name="students_sponsors_count"),
]
