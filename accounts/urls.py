from django.urls import path
from . views import *
from . forms import *
from django.contrib.auth import views as auth_view


urlpatterns = [
    path('',Signup.as_view(), name='register'),
    path('login/', auth_view.LoginView.as_view(template_name = 'login.html', authentication_form = LoginForm), name='login'),
    path('logout/', logout, name='logout')
]