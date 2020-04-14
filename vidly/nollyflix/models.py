from django.db import models


"""
field:
    Char
    Int
    Float
    Boolean


"""

# Create your models here.

class Genre(models.Model):
    name = models.CharField(max_length= 255)

    def __str__(self):
        return self.name
    
class Movie(models.Model):
    title = models.CharField(max_length = 255)
    star = models.CharField(max_length = 255)
    release_year = models.IntegerField()
    price = models.FloatField()
    in_stock = models.IntegerField()
    # have 1 to many relations with genre
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    in_4k = models.BooleanField()
    director = models.CharField(max_length = 255)
    image_url = models.TextField()

    #def __str__(self):
    #   return str(self.release_year) + self.title

