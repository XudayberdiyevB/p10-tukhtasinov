from django.urls import path

from students.views import (
    StudentDetailView,
    StudentsAndSponsorsCountApi,
    StudentsListView,
)


app_name = "students"

urlpatterns = [
    path("", StudentsListView.as_view(), name="students_list"),
    path("<int:pk>/", StudentDetailView.as_view(), name="student_detail"),
    path("student_sponsor_count/", StudentsAndSponsorsCountApi.as_view(), name="students_sponsors_count"),
]
