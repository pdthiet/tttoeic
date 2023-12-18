from django.urls import path
from . import views

urlpatterns = [
    path('all', views.get_all_vocabulary, name='all_vocabulary'),
    path('create', views.create_vocabulary, name='create_vocabulary'),
    path('update', views.update_vocabulary, name='update_vocabulary'),
    path('delete', views.delete_vocabulary, name='delete_vocabulary'),
]
