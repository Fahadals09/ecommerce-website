# Generated by Django 3.2.7 on 2021-09-21 21:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_products_colors'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='products',
            name='subtitle',
        ),
    ]
