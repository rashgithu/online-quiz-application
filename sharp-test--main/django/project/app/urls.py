from django.urls import path
from . import views

urlpatterns=[
    path('',views.webpage1, name='index'),#views is importing a function named index
]