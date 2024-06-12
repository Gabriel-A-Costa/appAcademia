from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Aparelho(models.Model):

    def __str__(self):
        return self.aparelho_name
    
    aparelho_name = models.CharField(max_length=200)
    aparelho_image = models.ImageField(upload_to='academia/aparelhos/', default="academia/aparelhos/default.jpg")
    users = models.ManyToManyField(User)

class Exercicio(models.Model):

    def __str__(self):
        return self.exercicio_type

    exercicio_type = models.CharField(max_length=200)
    exercicio_image = models.ImageField(upload_to='academia/exercicio/', default="academia/exercicio/default.jpg")
    users = models.ManyToManyField(User)

class Treinos(models.Model):

    def __str__(self):
        return self.treino_name
    
    treino_name = models.CharField(max_length=200)
    treino_image = models.ImageField(upload_to='academia/treino/', default="academia/treino/default.jpg")
    users = models.ManyToManyField(User)

class Room(models.Model):

    def __str__(self):
        return self.title
    
    host = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    message = models.TextField(max_length=800, null=True, blank=True)
    update = models.DateTimeField(auto_now_add=True)