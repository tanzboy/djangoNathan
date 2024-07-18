from django.urls import path
from . import views

urlpatterns = [
    path('', views.index)#karena memanggil views maka import views
]