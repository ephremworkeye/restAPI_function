from django.urls import path
from . import views, api_views

urlpatterns = [
    path('movie_lists', api_views.movie_lists),
    path('cat_lists', api_views.cat_lists),
    path('cat_lists/<int:id>', api_views.cat_detail),
    path('api/first_api_view', api_views.first_api_view)
]
