from django.urls import path, include
from . import views

urlpatterns = [
    path('vip_price/all', views.get_all_vip_price, name='all_vip_price'),
    path('vip_function/all', views.get_all_vip_function, name='get_all_vip_function'),
    path('vip_price/update', views.update_vip_price, name='update_vip_price'),
    path('vip_price/delete', views.delete_vip_price, name='delete_vip_price'),
    path('vip_price/create', views.create_vip_price, name='create_vip_price'),
]
