from django.contrib import admin
from .models import Genre, Movie

# Register your models here.
class MovieAdmin(admin.ModelAdmin):
    list_display=['title', ]

admin.site.register(Genre)
admin.site.register(Movie, MovieAdmin)

