from django.contrib import admin
from app1.models import student

class student_admin(admin.ModelAdmin):
    list_display = ['name','pin']
admin.site.register(student,student_admin)

