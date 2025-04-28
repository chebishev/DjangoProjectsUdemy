from django.db import models

# Create your models here.
class MovieData(models.Model):
    name = models.CharField(max_length=200)
    duration = models.FloatField()
    rating = models.FloatField()
    genre = models.CharField(max_length=200, default="action")
    image = models.ImageField(upload_to="movie_images/", default="movie_images/default.jpg")

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'Movie data'
