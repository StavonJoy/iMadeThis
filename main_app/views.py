from django.shortcuts import render, redirect
from .models import Craft, Photo, Material
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
import uuid
import boto3
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

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
  materials_craft_doesnt_have = Material.objects.exclude(id__in = craft.materials.all().values_list('id'))
  return render(request, 'crafts/detail.html', { 'craft': craft, 'materials': materials_craft_doesnt_have })

class CraftCreate(CreateView):
  model = Craft
  fields = ['name', 'type', 'hours', 'description']
  success_url= '/crafts/'

  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)

class CraftUpdate(UpdateView):
  model = Craft
  fields = ['name', 'type', 'hours', 'description', 'material']

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

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)

class MaterialList(ListView):
  model = Material

class MaterialDetail(DetailView):
  model = Material

class MaterialCreate(CreateView):
  model = Material
  fields = '__all__'

class MaterialUpdate(UpdateView):
  model = Material
  fields = '__all__'

class MaterialDelete(DeleteView):
  model = Material
  success_url = '/materials/'

def assoc_material(request, craft_id, material_id):
  Craft.objects.get(id=craft_id).materials.add(material_id)
  return redirect('detail', craft_id=craft_id)