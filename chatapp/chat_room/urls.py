from django.urls import path
from chat_room import views

urlpatterns = [
    path('', views.register_user, name="register"),
    path('login', views.login_user, name="login"),
    path('chat_room/<int:user_id>', views.chat_room, name="chat_room")
]