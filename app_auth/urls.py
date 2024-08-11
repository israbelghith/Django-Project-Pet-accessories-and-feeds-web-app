from django.urls import path
from .views import *

urlpatterns = [
  #  path('login/', login_Projet, name='login_Projet'),
    path('register/', register, name='register'),
    path('login/', login, name='login'),
    path('logout/', logout_User, name='logout_User'),
]
