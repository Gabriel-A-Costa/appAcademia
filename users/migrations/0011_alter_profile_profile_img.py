# Generated by Django 5.0.2 on 2024-03-21 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_remove_profile_email_remove_profile_first_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_img',
            field=models.ImageField(default='/', upload_to='Images', max_length=100),
        ),
    ]