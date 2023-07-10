from django.db import models

# Create your models here.


class TimestampModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class University(TimestampModel):
    name = models.CharField(max_length=200)
