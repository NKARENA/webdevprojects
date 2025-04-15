from django.contrib import admin
from testapp.models import Company

class CompanyAdmin(admin.ModelAdmin):
    list_display = ['name','location','ceo']

# Register your models here.
admin.site.register(Company, CompanyAdmin)
    
