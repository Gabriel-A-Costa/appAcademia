# Generated by Django 5.0.2 on 2024-02-15 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aparelho',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aparelho_name', models.CharField(max_length=200)),
                ('aparelho_image', models.CharField(default='https://photos.google.com/u/2/photo/AF1QipPzhvjKJoKzC0O9YTZoKz_LV61X16NObKsZUitn', max_length=500)),
            ],
        ),
    ]