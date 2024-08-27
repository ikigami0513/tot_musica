from typing import List
import uuid, os
from django.db import models
from .fields import AudioFileField

def artist_file_path(instance, filename):
    base_filename, file_extension = os.path.splitext(filename)
    return os.path.join(f"artists/{instance.id}.{uuid.uuid4()}.{file_extension}")

class Artist(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    picture = models.ImageField(upload_to=artist_file_path, null=True)

class Genre(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50)

def music_song_file_path(instance, filename):
    base_filename, file_extension = os.path.splitext(filename)
    return os.path.join(f"musics/audio/{instance.id}.{uuid.uuid4()}.{file_extension}")

def music_picture_file_path(instance, filename):
    base_filename, file_extension = os.path.splitext(filename)
    return os.path.join(f"musics/picture/{instance.id}.{uuid.uuid4()}.{file_extension}")

class Music(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    file = AudioFileField(upload_to=music_song_file_path)
    lyrics = models.TextField(null=True, blank=True)
    artists = models.ManyToManyField(Artist, blank=True, related_name="musics")
    genres = models.ManyToManyField(Genre, blank=True, related_name="musics")
    picture = models.ImageField(upload_to=music_picture_file_path, null=True, blank=True)

def album_picture_file_path(instance, filename):
    base_filename, file_extension = os.path.splitext(filename)
    return os.path.join(f"albums/picture/{instance.id}.{uuid.uuid4()}.{file_extension}")

class Album(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    musics = models.ManyToManyField(Music, blank=True, related_name="albums")
    picture = models.ImageField(upload_to=album_picture_file_path, null=True, blank=True)

    @property
    def artists(self) -> List[Artist]:
        return Artist.objects.filter(musics__albums=self).distinct()
