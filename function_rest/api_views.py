from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Category, Movie
from .serializers import CategorySerializer, MovieSerializer

@api_view()
def first_api_view(request):
    num_categoies = Category.objects.count()
    num_movies = Movie.objects.count()
    return Response({'num_categories':num_categoies, 'num_movies':num_movies})

@api_view()
def cat_lists(request):
    cat_lists = Category.objects.all()
    cat_serializer = CategorySerializer(cat_lists, many=True)
    return Response(cat_serializer.data)

@api_view()
def movie_lists(request):
    movie_lists = Movie.objects.all()
    movie_serializer = MovieSerializer(movie_lists, many=True)
    return Response(movie_serializer.data)

@api_view()
def cat_detail(request, id):
    cat_detail = get_object_or_404(Category, id=id)
    cat_serializer = CategorySerializer(cat_detail)
    return Response(cat_serializer.data)