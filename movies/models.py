from django.db import models
from django.utils import timezone

class Genre(models.Model):
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name
    
class Movie(models.Model):
    title = models.CharField(max_length=255)
    released_year = models.IntegerField()
    number_in_stoke = models.IntegerField()
    daily_rate = models.FloatField()
    genre = models.ForeignKey(Genre,on_delete=models.CASCADE)
    deta_created = models.DateTimeField(default=timezone.now)#we put a reference instead the method(timezone.now())
    
    def __str__(self):
        return self.title