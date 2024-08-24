from django.urls import path
from chat_room import views

urlpatterns = [
    path('', views.home, name="home")
]