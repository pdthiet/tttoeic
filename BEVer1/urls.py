"""BEVer1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/student/', include('student.urls')),
    path('api/vocabulary/', include('vocabulary.urls')),
    path('api/note/', include('note.urls')),
    path('api/part/', include('part.urls')),
    path('api/exam_title/', include('exam_title.urls')),
    path('api/examination/', include('examination.urls')),
    path('api/result/', include('result.urls')),
    path('api/vip/', include('vip.urls')),
    path('api/chat/', include('chat.urls')),
]
