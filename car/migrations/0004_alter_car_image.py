# Generated by Django 4.1.3 on 2023-01-24 21:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0003_car_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='image',
            field=models.ImageField(default=None, upload_to='car_image'),
        ),
    ]
