from rest_framework import serializers
from .models import Album, Musician

class MuscianSerializer(serializers.Serializer):
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    instrument = serializers.CharField()

class AlbumSerializer(serializers.Serializer):
    name = serializers.CharField()
    release_date = serializers.DateField()
    num_stars = serializers.IntegerField()
    artist = MuscianSerializer()
    