from django.db import models

# Create your models here.

class Vilao(models.Model):

    armas_opcoes = [
        ('machado', 'Machado'),
        ('escada', 'Espada'),
        ('tesoura', 'Tesoura'),
        ('veneno', 'Tesoura'),
        ('pexeira', 'Pexeira'),
        ('ak47', 'Ak-47'),
        ('almofada', 'Almofada')
    ]

    nivel_valor = [ 
        (1,1),
        (2,2),
        (3,3),
        (4,4),
        (5,5),
    ]

    nome = models.CharField(max_length=30)
    categoria = models.CharField(max_length=10)
    habilidades = models.TextField()
    mortes = models.PositiveIntegerField()
    armas = models.CharField(max_length=20, choices=armas_opcoes)
    nivel_maldade = models.PositiveIntegerField(choices=nivel_valor)
    vivo = models.BooleanField(default=True)
    foto = models.ImageField(upload_to='')