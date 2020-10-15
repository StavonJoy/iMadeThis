from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
# Create your models here.


class Material(models.Model):
  name = models.CharField(max_length=50)

  def __str__(self):
    return self.name
  
  def get_absolute_url(self):
    return reverse('materials_detail', kwargs={'pk': self.id})

class Craft(models.Model): 
  name = models.CharField(max_length=100)
  type = models.CharField(max_length=100)
  hours = models.IntegerField()
  description = models.CharField(max_length=300)
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  materials = models.ManyToManyField(Material)

  def __str__(self):
    return self.name
    
  def get_absolute_url(self):
    return reverse('detail', kwargs={'craft_id': self.id})

class Photo(models.Model):
  url = models.CharField(max_length=200)
  craft = models.ForeignKey(Craft, on_delete=models.CASCADE)

  def __str__(self):
    return f"Photo for craft_id: {self.craft_id} @{self.url}"