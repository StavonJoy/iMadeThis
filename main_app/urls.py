from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('crafts/', views.crafts_index, name='index'),
  path('crafts/<int:craft_id>/', views.crafts_detail, name='detail'),
  path('crafts/create/', views.CraftCreate.as_view(), name='crafts_create'),
  path('crafts/<int:pk>/update/', views.CraftUpdate.as_view(), name='crafts_update'),
  path('crafts/<int:pk>/delete/', views.CraftDelete.as_view(), name='crafts_delete'),
  path('crafts/<int:craft_id>/add_photo/', views.add_photo, name='add_photo'),
  path('accounts/signup/', views.signup, name='signup'),
  path('materials/', views.MaterialList.as_view(), name="material_index"),
]