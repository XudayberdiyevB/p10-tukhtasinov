from django.contrib import admin

from .models import Sponsor, Student, StudentSponsor


admin.site.register(Student)
admin.site.register(StudentSponsor)
