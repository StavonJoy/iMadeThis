from django.shortcuts import render
from django.http import HttpResponse
from .models import Craft

def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def crafts_index(request):
  crafts = Craft.objects.all()
  return render(request, 'crafts/index.html', { 'crafts': crafts })
