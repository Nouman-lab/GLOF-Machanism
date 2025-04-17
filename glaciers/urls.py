from django.urls import path
from . import views

app_name = 'glaciers'

urlpatterns = [
    path('', views.home, name='home'),
    path('glaciers/', views.glacier_list, name='glacier_list'),
    path('glaciers/<int:pk>/', views.glacier_detail, name='glacier_detail'),
] 