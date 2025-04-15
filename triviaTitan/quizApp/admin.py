from django.contrib import admin
from quizApp.models import Quiz


class QuizAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Quiz._meta.get_fields()]


# Register your models here.
admin.site.register(Quiz, QuizAdmin)
