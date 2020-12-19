
from django.urls import path
from .views import home,index, bangladesh, sodesh,pricing,about_pims, contact

urlpatterns = [

    path('', index, name = 'index'),
    path('home', home, name = 'index_2'),
    path('pricing', pricing, name = 'pricing'),
    path('bangladeshData', bangladesh, name='bangladeshData'),
    path('sodeshData', sodesh, name='sodeshData'),
    path('about_pims',about_pims,name='about_pims'),
    path('contact',contact,name='contact'),
    path('contact',contact,name='contact'),
]