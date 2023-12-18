from django.urls import path, include
from . import views

urlpatterns = [
    path('create', views.create_note, name='create_note'),
    path('get', views.get_note_by_firebase_id, name='get_note_by_firebase_id'),
    path('update/<int:id>', views.update_note, name='update_note'),
    path('delete/<int:id>', views.delete_note, name='delete_note'),
]
