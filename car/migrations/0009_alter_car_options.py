# Generated by Django 4.1.3 on 2023-02-06 02:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0008_remove_car_contact_remove_car_contact_name'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='car',
            options={'permissions': (('can_add_cost_price', 'Can add cost price'),)},
        ),
    ]
