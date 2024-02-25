from django.urls import path     
from . import views

urlpatterns = [
    path('', views.index),	   
    path('apps', views.apps),	   
    path('apps2', views.apps2),	 
    path('soups', views.soups),	 
    path('steaks', views.steaks),	 
    path('steaks2', views.steaks2),	 
    path('seafood', views.seafood),	 
    path('addons', views.addons),	 
    path('sides', views.sides),	 
    path('desserts', views.desserts),	 
    path('desserts2', views.desserts2),	 
    path('bar', views.bar),	 
    path('page2', views.page2),	 
    path('page1', views.page1),	 
    path('HH', views.HH),	 
    path('HH2', views.HH2),	 
    path('HH3', views.HH3),	 
    
    path('create/<str:name>', views.create),
    path('getPool', views.getPool),
    path('toggle/<str:name>', views.toggle),

]