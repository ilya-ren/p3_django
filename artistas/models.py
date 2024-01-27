from django.db import models

# Create your models here.


class Artista(models.Model):
    rut            = models.CharField(primary_key= True, max_length=10)
    nombre         = models.CharField(max_length=20)
    ap_paterno     = models.CharField(max_length=20)
    ap_materno     = models.CharField(max_length=20)
    fec_nacimiento = models.DateField(blank= False, null= False)
    id_genero      = models.ForeignKey('Genero', on_delete=models.CASCADE, db_column= 'id_genero')
    telefono       = models.CharField(max_length=45)
    email          = models.EmailField(unique=True, max_length=100, blank=False, null=True)
    direccion      = models.CharField(max_length=50, blank=True, null=True)
    activo         = models.IntegerField()

    def __str__(self):
        return str(self.nombre)+ " " +str(self.ap_paterno)



class Genero(models.Model):
    id_genero= models.AutoField(db_column='idGenero',primary_key=True)
    genero   = models.CharField(max_length=20, blank= False, null= False)

    def __str__(self):
        return str(self.genero)