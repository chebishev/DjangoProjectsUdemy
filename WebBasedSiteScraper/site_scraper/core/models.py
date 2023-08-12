from django.db import models

# Create your models here.


class Link(models.Model):

    MAX_LENGTH = 1000

    address = models.CharField(max_length=MAX_LENGTH, null=True, blank=True)
    name = models.CharField(max_length=MAX_LENGTH, null=True, blank=True)

    def __str__(self):
        return self.name
