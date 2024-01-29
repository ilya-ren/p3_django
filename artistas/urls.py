
from django.urls import path
from  .  import views



urlpatterns= [
    path('index', views.index, name='index'),
    path('listadoSQL', views.listadoSQL, name='listadoSQL'),
    path('crud', views.crud, name='crud'),

    path('artistasAdd', views.artistasAdd, name='artistasAdd'),
    path('artistas_del/<str:pk>', views.artistas_del, name='artistas_del'),
    path('artistas_finEdit/<str:pk>', views.artistas_finEdit, name='artistas_finEdit'),
    path('artistasUpdate', views.artistasUpdate, name='artistasUpdate'),
   
]

