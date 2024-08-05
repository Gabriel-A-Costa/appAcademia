# Generated by Django 5.0.2 on 2024-07-11 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0042_training_tipo_treino'),
    ]

    operations = [
        migrations.AlterField(
            model_name='antropometria',
            name='abdome',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='antropometria',
            name='ante_braco_direito',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='antropometria',
            name='ante_braco_esquerda',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='antropometria',
            name='braco_direito',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='antropometria',
            name='braco_esquerda',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='antropometria',
            name='cintura',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='antropometria',
            name='coxa_direito',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='antropometria',
            name='coxa_esquerda',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='antropometria',
            name='estatura',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='antropometria',
            name='gordura',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='antropometria',
            name='gordura_viceral',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='antropometria',
            name='idade_corporal',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='antropometria',
            name='imc',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='antropometria',
            name='massa_corporal',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='antropometria',
            name='massa_corporal_2',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='antropometria',
            name='metabolismo',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='antropometria',
            name='ombro',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='antropometria',
            name='panturrilha_direito',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='antropometria',
            name='panturrilha_esquerda',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='antropometria',
            name='pescoco',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='antropometria',
            name='quadril',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='antropometria',
            name='torax',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]