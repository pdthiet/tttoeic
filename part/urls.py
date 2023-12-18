from django.urls import path, include
from . import views

urlpatterns = [
    path('all', views.all_part, name='all_part'),
]
