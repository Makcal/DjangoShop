# Generated by Django 3.0.7 on 2020-07-18 00:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_auto_20200718_0321'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Цена'),
        ),
    ]
