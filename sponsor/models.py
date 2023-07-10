from django.db import models
from django.utils.translation import gettext_lazy as _


class Sponsor(models.Model):
    class StatusChoices(models.TextChoices):
        NEW = "new", _("New")
        IN_PROCESS = "in_process", _("In process")
        CONFIRMED = "confirmed", _("Confirmed")
        CANCELLED = "cancelled", _("Cancelled")

    full_name = models.CharField(max_length=250)
    phone = models.CharField(max_length=30)
    amount = models.PositiveBigIntegerField()
    is_organization = models.BooleanField()
    status = models.CharField(max_length=30, choices=StatusChoices.choices)
    created_at = models.DateTimeField(auto_now_add=True)
    organization_name = models.CharField(max_length=250)

    def __str__(self):
        return self.full_name

    @property
    def spent_money(self):
        return self.students.aggregate(spent_money=sum("amount")).get("spent_money")
