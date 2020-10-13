from django.shortcuts import render, redirect
from .models import Craft, Photo
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
import uuid
import boto3

S3_BASE_URL = 'https://s3.us-east-2.amazonaws.com/'
BUCKET = 'imadethiss'

def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def crafts_index(request):
  crafts = Craft.objects.all()
  return render(request, 'crafts/index.html', { 'crafts': crafts })

def crafts_detail(request, craft_id):
  craft = Craft.objects.get(id=craft_id)
  return render(request, 'crafts/detail.html', { 'craft': craft })

class CraftCreate(CreateView):
  model = Craft
  fields = ['name', 'type', 'hours', 'description']
  success_url= '/crafts/'

  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)

class CraftUpdate(UpdateView):
  model = Craft
  fields = '__all__'

class CraftDelete(DeleteView):
  model = Craft
  success_url = '/crafts/'

def add_photo(request, craft_id):
    photo_file = request.FILES.get('photo-file', None)
    if photo_file:
        s3 = boto3.client('s3')
        key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
        try:
            s3.upload_fileobj(photo_file, BUCKET, key)
            url = f"{S3_BASE_URL}{BUCKET}/{key}"
            photo = Photo(url=url, craft_id=craft_id)
            photo.save()
        except:
            print('An error occurred uploading file to S3')
    return redirect('detail', craft_id=craft_id)