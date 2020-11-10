
from django.urls import path
from .views import index, bangladesh

urlpatterns = [

    path('', index, name = 'index'),
    path('bangladeshData', bangladesh, name='bangladeshData'),
]