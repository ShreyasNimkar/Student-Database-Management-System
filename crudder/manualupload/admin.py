from django.contrib import admin
from import_export.admin import ImportExportActionModelAdmin
from manualupload.models import Student
# Register your models here.


@admin.register(Student)
class StudentAdmin(ImportExportActionModelAdmin):
    list_display = ('name', 'email', 'rollno', 'grade', 'division', 'mobno')
