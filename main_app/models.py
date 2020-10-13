from django.db import models
from django.urls import reverse

# Create your models here.


class Craft(models.Model): 
  name = models.CharField(max_length=100)
  type = models.CharField(max_length=100)
  hours = models.IntegerField()
  description = models.CharField(max_length=300)

  def __str__(self):
    return self.name
  def get_absolute_url(self):
    return reverse('detail', kwargs={'craft_id': self.id})

