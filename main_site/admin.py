from django.contrib import admin
from . import models


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(models.Applicant)
class ApplicantAdmin(admin.ModelAdmin):
    list_display = ('id', 'last_name', 'first_name')
