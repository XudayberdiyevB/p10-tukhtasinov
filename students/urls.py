from django.urls import path

from students.views import StudentListCreateView, StudentsAndSponsorsCountApi, StudentDetailView

app_name = "students"

urlpatterns = [
    path("student_sponsor_count", StudentsAndSponsorsCountApi.as_view(), name="students_sponsors_count"),
    path("", StudentListCreateView.as_view(), name="student_list_create"),
    path('<int:pk>', StudentDetailView.as_view(), name="student_detail")
]
