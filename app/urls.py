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
    
    path('create/<str:name>', views.create),
    path('getPool', views.getPool),

]