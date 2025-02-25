"""Project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path
from ott import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.openPage, name="index"),
    path('songs/', views.songsPage, name="songs"),
    path('series/', views.seriesPage, name="movies"),
    path('home/', views.openPage, name="index"),
    path('mylist/', views.mylistPage, name="mylist"),
    path('login/', views.loginPage, name="login"),
    path('register/', views.registerPage, name="register"),
    path('vpage/', views.vPage, name="vpage"),
    path('seemore/', views.seemorePage, name="seemore"),
    path('watchhistory/', views.watchhistoryPage, name="watchhistory"),
    path('liked/', views.likedPage, name="liked"),
]
