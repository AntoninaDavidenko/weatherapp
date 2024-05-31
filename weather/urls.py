from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_page, name='main'),
    path('home', views.index, name='home'),
    path('meteo/<uuid:city_id>', views.delete, name='delete'),
]
