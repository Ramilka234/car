# Generated by Django 5.0.6 on 2024-05-28 17:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inspection', '0002_order'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Order',
        ),
    ]