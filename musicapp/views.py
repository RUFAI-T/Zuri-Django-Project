from django.shortcuts import render
from .serializers import ArtisteSerials, SongSerials, LyricSerials
from .models import Artiste, Song, Lyric
from rest_framework import generics


# Create your views here.
def home(request):
	return render(request, "home.html", {})

def about(request):
	return render(request, 'about.html', {})




class ListArtisteApi(generics.ListAPIView):
	queryset = Artiste.objects.all()
	serializer_class = ArtisteSerials

class CreateArtisteApi(generics.CreateAPIView):
	queryset = Artiste.objects.all()
	serializer_class = ArtisteSerials



class ListSongApi(generics.ListAPIView):
	queryset = Song.objects.all()
	serializer_class = SongSerials

class CreateSongApi(generics.CreateAPIView):
	queryset = Song.objects.all()
	serializer_class = SongSerials


class ListLyricApi(generics.ListAPIView):
	queryset = Lyric.objects.all()
	serializer_class = LyricSerials

class CreateLyricApi(generics.CreateAPIView):
	queryset = Lyric.objects.all()
	serializer_class = LyricSerials



