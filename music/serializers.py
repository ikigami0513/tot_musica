from rest_framework import serializers
from .models import Artist, Genre, Music, Album

class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ['id', 'name', 'picture']

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['id', 'name']

class MusicSerializer(serializers.ModelSerializer):
    artists = ArtistSerializer(many=True, read_only=True)
    genres = GenreSerializer(many=True, read_only=True)

    class Meta:
        model = Music
        fields = ['id', 'title', 'file', 'lyrics', 'artists', 'genres', 'picture']

class AlbumSerializer(serializers.ModelSerializer):
    musics = MusicSerializer(many=True, read_only=True)
    artists = ArtistSerializer(many=True, read_only=True, source='artists')  # Utilise la propriété artists du modèle Album

    class Meta:
        model = Album
        fields = ['id', 'title', 'musics', 'picture', 'artists']
