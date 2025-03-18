from django.db import models

# Create your models here.
class Expense(models.Model):
    name = models.CharField(max_length=100)
    amount = models.IntegerField()
    category = models.CharField(max_length=50)
    date = models.DateField(auto_now=True)

    # To show the name instead of "Expense object (1)" in the admin panel
    def __str__(self):
        return self.name
