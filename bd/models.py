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

class Sodesh(models.Model):
    geom = gis_model.PolygonField(srid=3857, blank=True, null=True)
    area_sqft = models.FloatField(blank=True, null=True)
    area_bigha = models.FloatField(blank=True, null=True)
    type = models.CharField(max_length=50, blank=True, null=True)
    katha = models.CharField(max_length=20, blank=True, null=True)
    plot_type = models.CharField(max_length=20, blank=True, null=True)
    area_k = models.CharField(max_length=20, blank=True, null=True)
    dimension = models.CharField(max_length=20, blank=True, null=True)
    plot_no = models.CharField(max_length=50, blank=True, null=True)
    katha_1 = models.CharField(max_length=20, blank=True, null=True)
    road_name = models.CharField(max_length=100, blank=True, null=True)
    owner_name = models.CharField(max_length=50, blank=True, null=True)
    father_field = models.CharField(db_column='father__', max_length=50, blank=True, null=True)  # Field renamed because it contained more than one '_' in a row. Field renamed because it ended with '_'.
    spouse_nam = models.CharField(max_length=50, blank=True, null=True)
    national_i = models.BigIntegerField(blank=True, null=True)
    tin_field = models.BigIntegerField(db_column='tin___', blank=True, null=True)  # Field renamed because it contained more than one '_' in a row. Field renamed because it ended with '_'.
    land_price = models.BigIntegerField(blank=True, null=True)
    mou_name = models.CharField(max_length=50, blank=True, null=True)
    mou_jl = models.CharField(max_length=50, blank=True, null=True)
    pur_date = models.DateField(blank=True, null=True)
    paid_date = models.DateField(blank=True, null=True)
    inst_date = models.DateField(blank=True, null=True)
    new = models.IntegerField(blank=True, null=True)
    land_cat = models.CharField(max_length=50, blank=True, null=True)
    road = models.CharField(max_length=50, blank=True, null=True)
    id_new = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sodesh'
