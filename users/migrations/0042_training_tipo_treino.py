# Generated by Django 5.0.2 on 2024-07-11 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0041_alter_training_qnt_repetitions'),
    ]

    operations = [
        migrations.AddField(
            model_name='training',
            name='tipo_treino',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]