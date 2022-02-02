from django.urls import path
from . import views

urlpatterns = [
    path('add_new_image/', views.add_image_view,name='add_image'),
]