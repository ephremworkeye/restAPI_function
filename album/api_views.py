from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import AlbumSerializer, MuscianSerializer
from .models import Album, Musician

@api_view()
def all_musician(request):
    musicians = Musician.objects.all()
    music_serailzer = MuscianSerializer(musicians, many=True)
    return Response(music_serailzer.data)

@api_view()
def all_albums(request):
    albums = Album.objects.all()
    album_serializer = AlbumSerializer(albums, many=True)
    return Response(album_serializer.data)