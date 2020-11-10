from django.shortcuts import render
from django.core.serializers import serialize
from django.http import HttpResponse
from .models import Bangladesh

# Create your views here.


def bangladesh(request):
    bangladeshData = serialize('geojson', Bangladesh.objects.all())
    return HttpResponse(bangladeshData, content_type='geojson')

def index(request):
    return render(request, 'index.html')
