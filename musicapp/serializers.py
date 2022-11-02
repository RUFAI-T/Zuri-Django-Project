from rest_framework import serializers
from .models import Artiste, Song, Lyric

class ArtisteSerials(serializers.ModelSerializer):
	class Meta:
		model = Artiste
		fields = "__all__"


class SongSerials(serializers.ModelSerializer):
	class Meta:
		model = Song
		fields = "__all__"


class LyricSerials(serializers.ModelSerializer):
	class Meta:
		model = Lyric
		fields = "__all__"