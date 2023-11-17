from django.urls import path
from taskboard import views
from .views import UserCreate

urlpatterns = [
    path('', views.index, name='index'),
    path('accounts/register/', UserCreate.as_view()),
]
