from django.shortcuts import render,get_object_or_404
from movies.models import Movie
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .serializers import MovieSerializer


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

# Create your views here.
