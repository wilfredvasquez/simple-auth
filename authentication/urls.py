from django.urls import path
from . import views

urlpatterns = [
    path(
        'auth/register',
        views.user_register,
        name='user_register'
    ),
    path(
        'auth/login',
        views.user_login,
        name='user_login'
    ),
]