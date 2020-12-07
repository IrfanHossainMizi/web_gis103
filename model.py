# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.contrib.gis.db import models


class AllPole7G(models.Model):
    gid = models.AutoField(primary_key=True)
    feeder = models.CharField(max_length=254, blank=True, null=True)
    f01_way_po = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    f02_feeder = models.CharField(max_length=254, blank=True, null=True)
    f03_pole_n = models.CharField(max_length=254, blank=True, null=True)
    yy = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    xx = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    f06_pole_s = models.CharField(max_length=254, blank=True, null=True)
    f07_pole_m = models.CharField(max_length=254, blank=True, null=True)
    f08_pole_t = models.CharField(max_length=254, blank=True, null=True)
    f09_pole_f = models.CharField(max_length=254, blank=True, null=True)
    f10_pole_e = models.CharField(max_length=254, blank=True, null=True)
    f11_conduc = models.CharField(max_length=254, blank=True, null=True)
    f12_conduc = models.CharField(max_length=254, blank=True, null=True)
    f13_conduc = models.CharField(max_length=254, blank=True, null=True)
    f14_transf = models.CharField(max_length=254, blank=True, null=True)
    f15_transf = models.CharField(max_length=254, blank=True, null=True)
    f16_transf = models.CharField(max_length=254, blank=True, null=True)
    f21_guy_un = models.CharField(max_length=254, blank=True, null=True)
    f22_jumper = models.CharField(max_length=254, blank=True, null=True)
    f23_device = models.CharField(max_length=254, blank=True, null=True)
    f24_device = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    f25_landma = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    f26_remark = models.CharField(max_length=254, blank=True, null=True)
    f11kv = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    f0_23kv = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    f0_440kv = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    f6_35kv = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    f33kv = models.CharField(max_length=254, blank=True, null=True)
    geom = models.PointField(srid=32642, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'all_pole_7g'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Bangladesh(models.Model):
    objectid = models.AutoField(db_column='OBJECTID', primary_key=True)  # Field name made lowercase.
    geom = models.MultiPolygonField(blank=True, null=True)
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


class Bangladesh2(models.Model):
    gid = models.AutoField(primary_key=True)
    shape_leng = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    shape_area = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
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
    objectid = models.FloatField(blank=True, null=True)
    geom = models.MultiPolygonField(srid=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bangladesh2'


class Demo(models.Model):
    name = models.TextField(blank=True, null=True)
    geometric_field = models.GeometryField(srid=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'demo'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Housingso(models.Model):
    id = models.BigIntegerField(primary_key=True)
    geom = models.PolygonField(srid=3857, blank=True, null=True)
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
        db_table = 'housingso'


class Housingsodesh(models.Model):
    id = models.BigIntegerField(primary_key=True)
    geom = models.MultiPolygonField(srid=3857, blank=True, null=True)
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

    class Meta:
        managed = False
        db_table = 'housingsodesh'


class NarayanganjTotalConsumers(models.Model):
    gid = models.AutoField(primary_key=True)
    consumer_l = models.CharField(max_length=50, blank=True, null=True)
    ac_number = models.CharField(max_length=50, blank=True, null=True)
    pole_nu = models.CharField(max_length=254, blank=True, null=True)
    page_nu = models.CharField(max_length=254, blank=True, null=True)
    consumer_n = models.CharField(max_length=254, blank=True, null=True)
    catagory = models.CharField(max_length=254, blank=True, null=True)
    connect_lo = models.CharField(max_length=254, blank=True, null=True)
    service_sp = models.CharField(max_length=254, blank=True, null=True)
    service_wi = models.CharField(max_length=254, blank=True, null=True)
    objectid = models.BigIntegerField(blank=True, null=True)
    geom = models.PointField(srid=32642, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'narayanganj total consumers'


class Sodesh(models.Model):
    geom = models.PolygonField(srid=3857, blank=True, null=True)
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
