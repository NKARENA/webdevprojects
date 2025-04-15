from django.contrib import admin
from testApp.models import Employee

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ["ename", "enum"]


# Register your models here.
admin.site.register(Employee, EmployeeAdmin)
