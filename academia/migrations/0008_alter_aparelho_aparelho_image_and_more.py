# Generated by Django 5.0.2 on 2024-03-21 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academia', '0007_exercicio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aparelho',
            name='aparelho_image',
            field=models.ImageField(default='https://lh3.googleusercontent.com/pw/ABLVV87cle3nCJz8sZI9wom9p8awgyA4bfNHYPIDqzpFgfpxS7woVqYIN0KokLtQl9OXJ7D1RH0bTabUIh2b3GQm-0E-Z88c05ZgJraEYxjW8vIOZwhd7SrX1RjUg6F1O1tkB8Pc3094OPPl8XKVp2c1ulY=w980-h980-s-no-gm?authuser=2', upload_to='Images'),
        ),
        migrations.AlterField(
            model_name='exercicio',
            name='exercicio_image',
            field=models.ImageField(default='https://lh3.googleusercontent.com/pw/ABLVV871yaY0M39J0tD8CgX8o6mYYKL5z3Xq9iZaNqJlq9ui_bL9KjUPtFHWN98Heu-7OVQQRTEicAO56ymDG2NxxMJIHXgs3XMevvA0eVptjTM-tH8vkZvfSuhjgJPzOlaI4QFsEnFHC0foc1DNTBzPCFI=w650-h661-s-no-gm?authuser=0', upload_to='Images'),
        ),
    ]
