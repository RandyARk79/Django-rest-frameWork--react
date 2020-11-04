from django.db import models
from 

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=55)
