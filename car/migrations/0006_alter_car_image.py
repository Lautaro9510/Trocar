# Generated by Django 4.1.3 on 2023-01-29 05:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0005_alter_car_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='car_image'),
        ),
    ]
