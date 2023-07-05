from django.db import models

# Create your models here.

class UserAnimalia(models.Model):
    emailUsuario = models.EmailField(unique=True, null=False, max_length=254, blank=False, primary_key=True, db_column='email_user')
    nameUsuario = models.CharField(max_length=100, blank=False, null=False)
    lastName = models.CharField(max_length=100, blank=False, null=False)
    password = models.CharField(max_length=50, blank=False, null=False)
    region = models.CharField(max_length=50, blank=False, null=False)
    provincia = models.CharField(max_length=50, blank=False, null=False)
    comuna = models.CharField(max_length=50, blank=False, null=False)
    address = models.CharField(max_length=100, blank=False, null=False)
    activo = models.IntegerField()
    
    def __str__(self):
        return str(self.nameUsuario) + " " + str(self.lastName)
    

    