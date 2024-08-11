"""
URL configuration for blogProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from blog.views import home,consulter,search,listeArticles,consulterProd,searchProd,listeProducts
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
        path('admin/', admin.site.urls),
        path('', home,name="home"),
        path('product/listeProducts/<int:pk>', listeProducts,name="listeProducts"),
        path('article/<int:id_article>', consulter,name="consulter"),
        path('product/recherche', searchProd,name="searchProd"),
        path('auth/', include("app_auth.urls")),
        path('myadmin/', include("app_adminInterface.urls")),
        #
        path('product/<int:id_product>', consulterProd,name="consulterProd"),
        
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
