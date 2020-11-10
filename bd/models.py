from django.db import models
from django.contrib.gis.db import models as gis_model

# Create your models here.

class Bangladesh(models.Model):
    objectid = models.AutoField(db_column='OBJECTID', primary_key=True)  # Field name made lowercase.
    geom = gis_model.MultiPolygonField(blank=True, null=True)
    shape_leng = models.FloatField(blank=True, null=True)
    shape_area = models.FloatField(blank=True, null=True)
    adm2_en = models.CharField(max_length=50, blank=True, null=True)
    adm2_pcode = models.CharField(max_length=50, blank=True, null=True)
    adm2_ref = models.CharField(max_length=50, blank=True, null=True)
    adm2alt1en = models.CharField(max_length=50, blank=True, null=True)
    adm2alt2en = models.CharField(max_length=50, blank=True, null=True)
    adm1_en = models.CharField(max_length=50, blank=True, null=True)
    adm1_pcode = models.CharField(max_length=50, blank=True, null=True)
    adm0_en = models.CharField(max_length=50, blank=True, null=True)
    adm0_pcode = models.CharField(max_length=50, blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    validon = models.DateField(blank=True, null=True)
    validto = models.DateField(blank=True, null=True)
    objectid_0 = models.BigIntegerField(db_column='objectid', blank=True, null=True)  # Field renamed because of name conflict.

    class Meta:
        managed = False
        db_table = 'bangladesh'
    

    # def __str__(self):
    #     return self.adm2_en