from django.urls import path
from taskboard import views

urlpatterns = [
    path('', views.index, name='index'),
]