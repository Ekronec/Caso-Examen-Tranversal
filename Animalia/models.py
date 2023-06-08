from django.db import models

# Create your models here.

class UserAnimalia(models.Model):
    emailUsuario = models.EmailField(unique=True, null=False, max_length=254, blank=False, primary_key=True, db_column='email_user')
    nameUsuario = models.CharField(max_length=100, blank=False, null=False)
    lastName = models.CharField(max_length=100, blank=False, null=False)
    password = models.CharField(max_length=50, blank=False, null=False)
    region = models.ForeignKey('region', on_delete=models.CASCADE, db_column='id_region')
    address = models.CharField(max_length=100, blank=False, null=False)
    activo = models.IntegerField()
    
class Region(models.Model):
    id_region = models.IntegerField(primary_key=True,  null=False, blank=False, db_column='id_region')
    name_region = models.CharField(max_length=50, blank=False,null=False)
    id_comuna = models.ForeignKey('comuna',db_column='id_comuna',  blank=False, null=False, on_delete=models.CASCADE)
    
class Comuna(models.Model):
    id_comuna = models.IntegerField(primary_key=True, blank=False, null=False,  db_column='id_comuna')
    name_comuna = models.CharField(max_length=50, blank=False, null=False)
    