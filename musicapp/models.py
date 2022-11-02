from django.db import models

# Create your models here.
from turtle import title
from django.db import models

# Create your models here.

class Artiste(models.Model):
    first_name=models.CharField(max_length= 150)
    last_name= models.CharField(max_length= 150)
    age=models.IntegerField()
    
    def __str__(self) :
        return str(self.first_name) + str(self.last_name)

class Song(models.Model):
    Artiste = models.ForeignKey("Artiste", on_delete=models.CASCADE)
    title=models.CharField(max_length= 150)
    date_released =models.DateTimeField()
    likes =models.IntegerField()
    artiste_id= models.IntegerField()
    
    def __str__(self) -> str:
        return str(self.title)


class Lyric(models.Model):
    Song= models.ForeignKey("Song",on_delete=models.CASCADE)
    content =models.CharField(max_length= 150)
    song_id = models.IntegerField()

    def __str__(self) -> str:
        return str(self.content)