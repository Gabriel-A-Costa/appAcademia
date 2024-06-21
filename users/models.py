from academia.models import Aparelho, Exercicio, Treinos
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django_resized import ResizedImageField

# Create your models here.  

class Training(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    type = models.ForeignKey(Exercicio, on_delete=models.CASCADE)
    aparelho = models.ForeignKey(Aparelho, on_delete=models.CASCADE)
    treino = models.ForeignKey(Treinos, on_delete=models.CASCADE, null=True, blank=True)
    tipo_treino = models.CharField(max_length=200, null=True, blank=True)
    tempo = models.CharField(max_length=200, null=True, blank=True)
    qnt_series = models.IntegerField(null=True, blank=True)
    qnt_repetitions = models.CharField(max_length=200, null=True, blank=True)
    date_creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.type} - {self.aparelho.aparelho_name}"
    

class Anamnese(models.Model):
    META = [
        ('Hiper.', 'Hiper.'),
        ('Cond. Físico', 'Cond. Físico'),
        ('Perda de Peso', 'Perda de Peso'),
        ('Qualidade de Vida', 'Qualidade de Vida'),
        ('RML', 'RML'),
    ]

    COLUNA = [
        ('Normal', 'Normal'),
        ('Hiper-lordose cervical', 'Hiper-lordose cervical'),
        ('Hiper-cifose', 'Hiper-cifose'),
        ('Hiper-lordose lombar', 'Hiper-lordose lombar'),
        ('Escoliose', 'Escoliose'),
    ]

    PRESSAO = [
        ('Normal', 'Normal'),
        ('Baixa', 'Baixa'),
        ('Alta', 'Alta'),
    ]

    OPCOES = [
        ('Sim', 'Sim'),
        ('Não', 'Não'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    # ANAMNESE
    meta = models.CharField(max_length=50, choices=META)
    pratica_atividades = models.CharField(max_length=5, choices=OPCOES)
    atividades_fisicas = models.CharField(max_length=300, null=True, blank=True)
    frequencia_atividades = models.CharField(max_length=300, null=True, blank=True)
    fuma = models.CharField(max_length=5, choices=OPCOES)
    tempo_fumante = models.CharField(max_length=200, null=True, blank=True)
    qnt_cigarro = models.IntegerField(null=True, blank=True)
    restricao = models.CharField(max_length=5, choices=OPCOES)
    tipos_restricao = models.CharField(max_length=200, null=True, blank=True)
    medicamento = models.CharField(max_length=5, choices=OPCOES)
    tipos_medicamento = models.CharField(max_length=200, null=True, blank=True)
    dores = models.CharField(max_length=5, choices=OPCOES) 
    tipos_dores = models.CharField(max_length=200, null=True, blank=True)
    acidente = models.CharField(max_length=5, choices=OPCOES) 
    tipos_acidentes = models.CharField(max_length=200, null=True, blank=True)
    dieta = models.CharField(max_length=5, choices=OPCOES)
    alergia = models.CharField(max_length=5, choices=OPCOES) 
    tipos_alergia = models.CharField(max_length=200, null=True, blank=True)
    controle_pressao = models.CharField(max_length=10, choices=PRESSAO) 
    pressao = models.CharField(max_length=200, null=True, blank=True)
    cardiaco = models.CharField(max_length=5, choices=OPCOES) 
    historico_cardiaco = models.CharField(max_length=200, null=True, blank=True)
    idade = models.IntegerField()
    coluna = models.CharField(max_length=200, choices=COLUNA) 
    data_anamnese = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username
    
class Antropometria(models.Model):

    AVALIADO = [
        ('Ativo', 'Ativo'),
        ('Sedentário', 'Sedentário'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    # Perimetria e Biometria (kg e cm)
    massa_corporal = models.FloatField(null=True, blank=True)
    estatura = models.FloatField(null=True, blank=True)
    pescoco = models.FloatField(null=True, blank=True)
    ombro = models.FloatField(null=True, blank=True)
    torax = models.FloatField(null=True, blank=True)
    cintura = models.FloatField(null=True, blank=True)
    abdome = models.FloatField(null=True, blank=True)
    quadril = models.FloatField(null=True, blank=True)

    #Perimetria direita
    braco_direito = models.FloatField(null=True, blank=True)
    ante_braco_direito = models.FloatField(null=True, blank=True)
    coxa_direito = models.FloatField(null=True, blank=True)
    panturrilha_direito = models.FloatField(null=True, blank=True)

    #Perimetria esquerda
    braco_esquerda= models.FloatField(null=True, blank=True)
    ante_braco_esquerda= models.FloatField(null=True, blank=True)
    coxa_esquerda= models.FloatField(null=True, blank=True)
    panturrilha_esquerda= models.FloatField(null=True, blank=True)

    imc = models.FloatField(null=True, blank=True)
    gordura = models.FloatField(null=True, blank=True)
    massa_corporal_2 = models.FloatField(null=True, blank=True)
    metabolismo = models.FloatField(null=True, blank=True)
    idade_corporal = models.FloatField(null=True, blank=True)
    gordura_viceral = models.FloatField(null=True, blank=True)

    avaliado = models.CharField(max_length=50, choices=AVALIADO, default='ativo')
    data_antropometria = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_img = ResizedImageField(size=[600, 600], quality=85, upload_to='academia/users/', default= 'academia/users/default-user.jpg')
    phone_number = models.CharField(max_length=16, null=True)

    trainings = models.ManyToManyField(Training)
    Anamnese = models.ManyToManyField(Anamnese)
    Antropometria = models.ManyToManyField(Antropometria)

    def __str__(self):
        return self.user.username


def creat_profile(sender, instance, created, **kwargs):
    if created and not hasattr(instance, 'profile'):
        user_profile = Profile(user=instance)
        user_profile.save()

post_save.connect(creat_profile, sender=User)