from django.urls import path, include
from . import views

urlpatterns = [
    path('get_audio_for_part', views.get_audio_for_part, name='get_audio_for_part'),
    path('get_audio_for_exam', views.get_audio_for_exam, name='get_audio_for_exam'),
    path('get_image', views.get_image, name='get_image'),
    path('get_examination', views.get_examination, name='get_examination'),
    path('get_reading_examination', views.get_reading_examination, name='get_reading_examination'),
    path('get_correct_answer', views.get_correct_answer, name='get_correct_answer'),
    path('get_examination_item', views.get_examination_item, name='get_examination_item'),
    path('get_part_question', views.get_part_question, name='get_part_question'), 
]
