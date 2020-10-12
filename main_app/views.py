from django.shortcuts import render
from django.http import HttpResponse

def home(request):
  return HttpResponse('<h1>Home</h1>')

def about(request):
  return render(request, 'about.html')

def crafts_index(request):
  return render(request, 'crafts/index.html', { 'crafts': crafts })

class Craft: 
  def __init__(self, name, type, hours, description):
    self.name = name
    self.type = type
    self.hours = hours
    self.description = description

crafts = [
  Craft('Knit Hat', 'knit', '2', 'A warm and cozy hat, made with chunky yarn and love.'),
]