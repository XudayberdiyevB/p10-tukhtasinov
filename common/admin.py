from django.contrib import admin

from .models import University


@admin.register(University)
class UniversityAdmin(admin.ModelAdmin):
    list_display = ["name"]
    search_fields = ["name"]
