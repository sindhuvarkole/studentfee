from django.contrib import admin
from app.models import Student
# Register your models here.
class Studentadmin(admin.ModelAdmin):
    list_display=('student','is_paid')
    search_fields=('student',)
admin.site.register(Student,Studentadmin)