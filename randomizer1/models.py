from django.db import models

# Create your models here.


class Randomizer1(models.Model):
    title = models.TextField()
    description = models.TextField()
    price = models.TextField()

