"""
URL configuration for project project.

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
from django.urls import path
from app.views import *
from . import views
#from.views import quiz_view

urlpatterns = [
    #path('admin/', admin.site.urls),
   # path('',include('app.urls'))
    path('',views.webpage1,name='webpage1'),
    path('login',views.webpage2,name='webpage2'),
    path('all-quiz',views.webpage3,name='webpage3'),
    path('computer',views.webpage4,name='webpage4'),
    path('leaderboard',views.webpage5,name='webpage5'),
    path('gk',views.webpage6,name='webpage6'),
    path('life',views.webpage7,name='webpage7'),
    path('math',views.webpage8,name='webpage8'),
    path('physics',views.webpage9,name='webpage9'),
   path('register',views.webpage10,name='webpage10'),
    path('blogs',views.webpage11,name='webpage11'),
     path('confirm',views.webpage12,name='webpage12'),
      path('contact-us',views.webpage13,name='webpage13'),
       path('dashboard',views.webpage14,name='webpage14'),
        path('downloads',views.webpage15,name='webpage15'),
         path('message',views.webpage16,name='webpage16'),
          path('profile-edit',views.webpage17,name='webpage17'),
           path('terms and condition',views.webpage18,name='webpage18'),
           path('profile',views.webpage19,name='webpage19'),
           path('question',views.home,name='home'),
           #path('quiz/',quiz_view,name="quiz_view")
           


]