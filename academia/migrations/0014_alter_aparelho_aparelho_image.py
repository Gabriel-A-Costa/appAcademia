# Generated by Django 5.0.2 on 2024-03-21 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academia', '0013_alter_aparelho_aparelho_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aparelho',
            name='aparelho_image',
            field=models.ImageField(default='https://lh3.googleusercontent.com/pw/ABLVV87cle3nCJz8sZI9wom9p8awgyA4bfNHYPIDqzpFgfpxS7woVqYIN0KokLtQl9OXJ7D1RH0bTabUIh2b3GQm-0E-Z88c05ZgJraEYxjW8vIOZwhd7SrX1RjUg6F1O1tkB8Pc3094OPPl8XKVp2c1ulY=w980-h980-s-no-gm?authuser=2', upload_to='aparelhos/'),
        ),
    ]