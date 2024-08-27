from django.contrib import admin
from . models import Artist, Genre, Music, Album

@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(Music)
class MusicAdmin(admin.ModelAdmin):
    list_display = ['title']

@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ['title']
