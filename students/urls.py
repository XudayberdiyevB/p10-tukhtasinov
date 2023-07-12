from django.urls import path

from students.views import StudentView, StudentsAndSponsorsCountApi


app_name = "students"

urlpatterns = [
    path("", StudentView.as_view(), name="students_list"),
    path("student_sponsor_count", StudentsAndSponsorsCountApi.as_view(), name="students_sponsors_count"),
]
