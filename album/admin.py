from django.contrib import admin
from .models import Musician, Album

# Register your models here.
@admin.register(Musician)
class MusicianAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'instrument']

@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ['artist', 'name', 'release_date', 'num_stars']
