from django.urls import path, include
from . import views

urlpatterns = [
    path('create_exam_result', views.create_exam_result, name='create_exam_result'),
    path('update_exam_result', views.update_exam_result, name='update_exam_result'),
    path('update_exam_score', views.update_exam_score, name='update_exam_score'),
    path('get_conversion_score', views.get_conversion_score, name='get_conversion_score'),
    path('get_student_answer', views.get_student_answer, name='get_student_answer'),
    path('get_latest_score', views.get_latest_score, name='get_latest_score'),
    path('create_part_result', views.create_part_result, name='create_part_result'),
    path('get_part_result', views.get_part_result, name='get_part_result'),
    path('part_result/get_by_user', views.get_part_result_by_user, name='get_part_result_by_user'),
    path('exam_result/get_by_user', views.get_exam_result_by_user, name='get_exam_result_by_user'),
]
