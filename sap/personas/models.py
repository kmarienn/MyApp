from django.db import models

# Create your models here.
class Curso(models.Model):
    nombre = models.CharField(max_length=50,null = True)
    horas = models.IntegerField(null = True)
    profesor = models.CharField(max_length=100,null = True)

    def __str__(self):
        return f'{self.nombre}'

class Persona(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    activo = models.BooleanField(default=True)
    curso = models.ForeignKey(Curso, on_delete = models.SET_NULL, null = True)

    def __str__(self):
        return f'id: {self.id} -{self.nombre} {self.apellido}'