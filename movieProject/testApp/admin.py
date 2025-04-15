from django.contrib import admin
from testApp.models import Movie
class MovieAdmin(admin.ModelAdmin):
    list_display = [ 'releasedate', 'moviename', 'hero', 'IMDB']
# Register your models here.
admin.site.register(Movie, MovieAdmin)