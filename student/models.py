from django.db import models

from sponsor.models import Sponsor
from university.models import University


class Student(models.Model):
    class StudentTypes(models.TextChoices):
        BACHELOR = "bachelor"
        MASTER = "master"
    
    full_name = models.CharField(max_length=100)
    degree = models.CharField(max_length=50, choices=StudentTypes.choices)
    tuition_fee = models.FloatField(default=0)
    created_at = models.DateTimeField(auto_now=True)
    university = models.ForeignKey("University", on_delete=models.CASCADE, related_name="students")

    def __str__(self):
        return self.full_name


class StudentSponsor(models.Model):
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    sponsor_id = models.ForeignKey(Sponsor, on_delete=models.CASCADE)
    amount = models.PositiveBigIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
