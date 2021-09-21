# Generated by Django 3.2.7 on 2021-09-21 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('setting', '0001_initial'),
        ('products', '0006_remove_products_colors'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='colors',
            field=models.ManyToManyField(blank=True, null=True, to='setting.Colors'),
        ),
    ]
