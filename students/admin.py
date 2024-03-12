from django.contrib import admin

from . models import *

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display=["first_name","last_name","email_id","phone_number"]


@admin.register(Departments)
class DepartmentAdmin(admin.ModelAdmin):
    list_display=["departments_name"]