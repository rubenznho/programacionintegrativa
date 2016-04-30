from django.db import models

class Usuario(models.Model):
        id = models.IntegerField(unique=True, primary_key=True)
        nombre = models.CharField(max_length=25, blank=True, null=True) 
        login = models.CharField(max_length=25, blank=True, null=True) 
        localidad = models.CharField(max_length=40, blank=True, null=True) 
        coordenadas = models.CharField(max_length=25, blank=True, null=True) 
        descripcion = models.CharField(max_length=250, blank=True, null=True) 
        dispositivom = models.IntegerField(blank=True, null=True)
        nseguidores = models.IntegerField(blank=True, null=True)
        namigos = models.IntegerField(blank=True, null=True)
        ntweetsp = models.IntegerField(blank=True, null=True)
        nfavoritos = models.IntegerField(blank=True, null=True)
        

        

