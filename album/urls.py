from django.urls import path
from . import api_views, views

urlpatterns = [
    path('all_musician', api_views.all_musician),
    path('all_albums', api_views.all_albums)
]
