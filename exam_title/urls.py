from django.urls import path, include
from . import views

urlpatterns = [
    path('all', views.all_exam_title, name='all_exam_title'),
    path('get/<str:exam_id>', views.get_exam_title, name='get_exam_title'),
    path('create_exam_info', views.create_exam_info, name='create_exam_info'),
    path('update_exam_info', views.update_exam_info, name='update_exam_info'),
    path('delete_exam_info', views.delete_exam_info, name='delete_exam_info'),
]
