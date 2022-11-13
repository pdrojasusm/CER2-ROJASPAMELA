from django.db import models

#superadministrador ; admin1234
#conserje_01 ; adminc1234
#conserje_02 ; admincc1234

class Correspondencia(models.Model):
    residencia = models.CharField(max_length = 10)
    class Estado(models.TextChoices):
        ENTREGADO = 'Entregado'
        RECIBIDO = 'Recibido'

    estado = models.CharField(max_length = 10,choices =Estado.choices,default=Estado.RECIBIDO)
    destinatario = models.CharField(max_length = 50)
    f_recepcion = models.DateTimeField()
    f_entrega = models.DateTimeField(null=True,blank=True)
    remitente = models.CharField(max_length = 50)
    conserje_rec = models.CharField(max_length = 50)
    conserje_ent = models.CharField(max_length = 50,null=True,blank=True)

    def __str__(self) -> str:
        return self.residencia

class Residencia(models.Model):
    r_id = models.CharField(max_length = 10)
    dueño = models.CharField(max_length = 50)
    c_celular = models.CharField(max_length = 20)
    c_email = models.EmailField()

    def __str__(self) -> str:
        return self.r_id
