from django.urls import path
from . import views

urlpatterns = [
    path('create', views.create_student, name = 'create_student'),
    path('check_new_firebase_id', views.check_new_firebase_id, name='check_new_firebase_id'),
    path('find', views.get_student_by_id, name = 'get_student_by_id'),
    path('update/<str:firebase_id>', views.update_student, name='update_student'),
    path('update_avatar/<str:firebase_id>', views.update_avatar, name='update_avatar'),
    path('update_vip', views.update_vip, name='update_vip'),
    path('check_vip_and_update', views.check_vip_and_update, name='check_vip_and_update'),
    path('check_superuser', views.check_superuser, name='check_superuser'),
    path('all', views.get_all_student, name='get_all_student'),
]
