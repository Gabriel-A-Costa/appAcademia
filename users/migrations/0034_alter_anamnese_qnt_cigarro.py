# Generated by Django 5.0.2 on 2024-06-05 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0033_anamnese_data_anamnese_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anamnese',
            name='qnt_cigarro',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]