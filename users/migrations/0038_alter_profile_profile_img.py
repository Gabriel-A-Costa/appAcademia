# Generated by Django 5.0.2 on 2024-06-11 23:50

import django_resized.forms
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0037_alter_antropometria_abdome_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_img',
            field=django_resized.forms.ResizedImageField(crop=None, default='users/default-user.jpg', force_format=None, keep_meta=True, quality=85, scale=None, size=[600, 600], upload_to='academia/users/'),
        ),
    ]
