# Generated by Django 5.0.2 on 2024-03-21 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academia', '0010_alter_aparelho_aparelho_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aparelho',
            name='aparelho_image',
            field=models.ImageField(default='aparelhos/default.jpg', upload_to='aparelhos/'),
        ),
    ]