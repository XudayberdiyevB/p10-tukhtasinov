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
    status = models.CharField(max_length=30, choices=StatusChoices.choices, default=StatusChoices.NEW)
    created_at = models.DateTimeField(auto_now_add=True)
    organization_name = models.CharField(max_length=250, null=True, blank=True)

    def __str__(self):
        return self.full_name