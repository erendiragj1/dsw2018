from django.db import models
from django.contrib.auth.models import User

# from django.contrib.auth.models import User, UserManager
# 4 de tamaño al id de servidores
# Create your models here.
class Usuario(models.Model):
    usr = models.CharField("Usuario", max_length=16,blank=False, null=False, primary_key=True)
    pwd = models.CharField("Contraseña", max_length=80,blank=False, null=False)
    nombres = models.CharField("Nombre", max_length=20, blank=False, null=False)
    apellidos = models.CharField("Apellido", max_length=20, blank=True, null=False)
    correo = models.EmailField(max_length=32, blank=True, null=True)
    numero = models.CharField(max_length=12, blank=True, null=True)
    chat_id = models.CharField(max_length=15, blank=True, null=True, default=0)
    token = models.CharField(max_length=16, blank=False, null=False, default=0)


class Servidor(models.Model):
    id = models.AutoField(primary_key=True, null=False)
    desc_srv = models.CharField(max_length=16, blank=False, null=False)
    ip_srv = models.CharField(max_length=12, blank=False, null=False)
    puerto = models.IntegerField(blank=False, null=False)
    estado = models.BooleanField("Activo/Inactivo", default=True)
    usr_srv = models.CharField("Usuario servidor", max_length=25, blank=False, null=False, default=" ")
    pwd_srv = models.CharField("Contraseña Servidor", max_length=50, blank=False, null=False, default="0")
    usr = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    puerto_tty = models.CharField("Puerto terminal", max_length=5, blank=False, null=False, default="0")
    llave = models.CharField(max_length=50, blank=False, null=False, default="0")


class Tglobal(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    token = models.CharField("Token Administrador global", max_length=16, blank=False, null=False, default=0)
    chat_id = models.CharField("Chat Id Administrador global", max_length=15, blank=True, null=True, default=0)


# admin_M0nS3rv1c3s2020
# (desc_srv = prueba1, ip_srv = 192.168.1.73, puerto = 8000, estado = True, usr= miguel)
