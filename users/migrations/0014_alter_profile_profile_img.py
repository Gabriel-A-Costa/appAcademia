# Generated by Django 5.0.2 on 2024-03-21 22:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0013_alter_profile_profile_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_img',
            field=models.ImageField(default='users/default.jpg', upload_to='users/'),
        ),
    ]
