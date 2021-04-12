from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'), # blank means home page
    path('delete/<str:pk>', views.delete, name='delete') # pk is a dynamic string variable
]