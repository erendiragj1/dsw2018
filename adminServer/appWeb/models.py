from django.db import models

# 4 de tamaño al id de servidores
# Create your models here.
class Usuario(models.Model):
    usr = models.CharField("Usuario", max_length=8, blank=False, null=False, primary_key=True)
    pwd = models.CharField("Contraseña", max_length=32, blank=False, null=False)
    nombres = models.CharField("Nombre", max_length=16, blank=False, null=False)
    apellidos = models.CharField("Apellido", max_length=16, blank=False, null=False)
    correo = models.EmailField(max_length=32, blank=False, null=True)
    numero = models.IntegerField(blank=False, null=True)
    chat_id = models.IntegerField(blank=False, null=False, default=0)
    token = models.IntegerField(blank=False, null=False, default=0)

class Servidor(models.Model):
    id = models.AutoField(primary_key=True, null=False)
    desc_srv = models.CharField(max_length=16, blank=False, null=False)
    ip_srv = models.CharField(max_length=12, blank=False, null=False)
    puerto = models.IntegerField(blank=False, null=False)
    usr = models.ForeignKey(Usuario, on_delete=models.CASCADE)
