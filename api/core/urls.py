from django.urls import path
from .views import home, register, user_login, user_logout, chatbot, chatbot_page, csrf_cookie

urlpatterns = [
    path('', home, name='home'),
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path("chatbot/page/", chatbot_page, name="chatbot_page"),
    path("chatbot/", chatbot, name="chatbot"),
    path('csrf-cookie/', csrf_cookie, name='csrf_cookie'),
]
