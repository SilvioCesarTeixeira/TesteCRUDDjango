from django.db import models


class Reservas(models.Model):
    Req_nome = models.CharField(max_length=30)
    Mat_nro = models.IntegerField()
    Curso_nome = models.CharField(max_length=30)
    Sala_nro = models.IntegerField()
    Data = models.DateField()
    Horario = models.TimeField()
