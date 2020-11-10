from django.contrib import admin
from .models import Bangladesh
from leaflet.admin import LeafletGeoAdmin

# Register your models here.


class BangladeshAdmin(LeafletGeoAdmin):
    list_display = ['adm2_en','adm1_en','shape_leng','date']
    list_filter = ['shape_leng','adm1_en']
    list_editable = ['date']

admin.site.register(Bangladesh, BangladeshAdmin)
