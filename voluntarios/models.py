from django.db import models

class Voluntario(models.Model):
    OPCIONES_TEMAS = [
        ('artistico', 'Artístico'),
        ('donaciones', 'Donaciones'),
        ('sede_comunal', 'Sede Comunal'),
        ('transporte', 'Transporte'),
        ('voluntariado_diverso', 'Voluntariado Diverso'),
        ('otros', 'Otros'),
    ]

    OPCIONES_TRANSPORTE = [
        ('moto', 'Moto'),
        ('carro', 'Carro'),
        ('bicicleta', 'Bicicleta'),
        ('a_pie', 'A pie'),
        ('transporte_publico', 'Transporte público'),
    ]

    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    telefono = models.CharField(max_length=15)
    email = models.EmailField()
    ciudad = models.CharField(max_length=100)
    comuna_o_corregimiento = models.CharField(max_length=100)
    tema_de_interes = models.CharField(max_length=50, choices=OPCIONES_TEMAS)
    medio_de_transporte = models.CharField(max_length=50, choices=OPCIONES_TRANSPORTE)
    apoyar_como_testigo_electoral = models.BooleanField()

    def __str__(self):
        return f'{self.nombre} {self.apellido}'
