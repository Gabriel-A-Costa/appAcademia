# Generated by Django 5.0.2 on 2024-06-05 23:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0035_antropometria_massa_corporal_2_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anamnese',
            name='frequencia_atividades',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]