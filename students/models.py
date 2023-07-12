from django.db import models
from django.utils.translation import gettext_lazy as _

from sponsors.models import Sponsor


class Student(models.Model):
    class StudentTypes(models.TextChoices):
        BACHELOR = "bachelors", _("Bachelors")
        MASTER = "master", _("Master")

    full_name = models.CharField(max_length=100)
    degree = models.CharField(max_length=50, choices=StudentTypes.choices)
    tuition_fee = models.FloatField(default=0)
    phone = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now=True)
    university = models.ForeignKey("common.University", on_delete=models.CASCADE, related_name="students")

    def __str__(self):
        return self.full_name


class StudentSponsor(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    sponsor = models.ForeignKey(Sponsor, on_delete=models.CASCADE, related_name="students")
    amount = models.PositiveBigIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
