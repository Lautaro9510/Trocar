# Generated by Django 4.1.3 on 2023-02-07 03:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='profile_picture',
            field=models.ImageField(default='user_default.png', null=True, upload_to='profile_images'),
        ),
    ]
