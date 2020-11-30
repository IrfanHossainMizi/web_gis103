
from django.urls import path
from .views import home,index, bangladesh

urlpatterns = [

    path('', index, name = 'index'),
    path('home', home, name = 'index_2'),
    path('bangladeshData', bangladesh, name='bangladeshData'),
]