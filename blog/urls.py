from django.urls import path
from . import views
urlpatterns=[
    path("",views.home,name="home"),
   # path("listeArticles",views.listArticles,name="listArticles")
]