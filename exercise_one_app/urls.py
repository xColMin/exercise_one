from django.urls import path
from exercise_one_app import views

urlpatterns = [
    path('', views.home, name='home'),
    path('user', views.user, name='user'),
]