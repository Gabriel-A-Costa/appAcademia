# Generated by Django 5.0.2 on 2024-04-24 20:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0017_alter_profile_profile_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_img',
            field=models.ImageField(default='media/users/default.jpg', upload_to='media/users/'),
        ),
    ]
