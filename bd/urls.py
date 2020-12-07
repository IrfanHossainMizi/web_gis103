
from django.urls import path
from .views import home,index, bangladesh, sodesh

urlpatterns = [

    path('', index, name = 'index'),
    path('home', home, name = 'index_2'),
    path('bangladeshData', bangladesh, name='bangladeshData'),
    path('sodeshData', sodesh, name='sodeshData'),
]