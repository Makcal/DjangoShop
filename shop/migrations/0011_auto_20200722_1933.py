# Generated by Django 3.0.8 on 2020-07-22 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0010_auto_20200722_0004'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=130, verbose_name='Название'),
        ),
    ]