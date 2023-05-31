from django.db import models

# Create your models here.

class user(models.Model):
    email = models.EmailField(unique=True, null=False, max_length=254, blank=False, primary_key=True, db_column='email_user')
    name = models.CharField(max_length=100, blank=False, null=False)
    lastName = models.CharField(max_length=100, blank=False, null=False)
    password = models.CharField(max_length=50, blank=False, null=False)
    region = models.ForeignKey('region', on_delete=models.CASCADE, db_column='id_region')
    
class region(models.Model):
    id_region = models.IntegerField(primary_key=True, max_length=50, null=False, blank=False, db_column='id_region')
    name_region = models.CharField(max_length=50, blank=False,null=False)
    id_comuna = models.ForeignKey(db_column='id_comuna', max_length=50, blank=False, null=False)
    
class comuna(models.Model):
    id_comuna = models.IntegerField(primary_key=True, blank=False, null=False, max_length=50, db_column='id_comuna')
    name_comuna = models.CharField(max_length=50, blank=False, null=False)
    