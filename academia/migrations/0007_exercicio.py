# Generated by Django 5.0.2 on 2024-02-24 17:10

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academia', '0006_delete_exercicio'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Exercicio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exercicio_type', models.CharField(max_length=200)),
                ('exercicio_image', models.CharField(default='https://lh3.googleusercontent.com/pw/ABLVV871yaY0M39J0tD8CgX8o6mYYKL5z3Xq9iZaNqJlq9ui_bL9KjUPtFHWN98Heu-7OVQQRTEicAO56ymDG2NxxMJIHXgs3XMevvA0eVptjTM-tH8vkZvfSuhjgJPzOlaI4QFsEnFHC0foc1DNTBzPCFI=w650-h661-s-no-gm?authuser=0', max_length=500)),
                ('users', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
