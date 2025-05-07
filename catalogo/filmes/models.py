from django.db import models

# Create your models here.
class Filme(models.Model):
    titulo = models.CharField(maax_length=100),
    decricao = models.TextField(),
    ano = models.IntegerField(),
    genero = models.CharField(max_length=50),
    capa = models.TextField(default="")

    def __str__(self):
        return self.titulo