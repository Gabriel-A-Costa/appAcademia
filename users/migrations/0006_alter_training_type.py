# Generated by Django 5.0.2 on 2024-02-23 21:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_alter_training_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='training',
            name='type',
            field=models.CharField(max_length=100),
        ),
    ]
