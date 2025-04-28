from django.db import models

# Create your models here.
class MovieData(models.Model):
    name = models.CharField(max_length=200)
    duration = models.FloatField()
    rating = models.FloatField()
    genre = models.CharField(max_length=200, default="action")


    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'Movie data'
        