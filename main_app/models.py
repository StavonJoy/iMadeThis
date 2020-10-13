from django.db import models

# Create your models here.


class Craft(models.Model): 
  name = models.CharField(max_length=100)
  type = models.CharField(max_length=100)
  hours = models.IntegerField()
  description = models.CharField(max_length=300)

  def __str__(self):
    return self.name

