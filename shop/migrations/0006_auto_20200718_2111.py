# Generated by Django 3.0.8 on 2020-07-18 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_auto_20200718_2104'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='photo',
            field=models.CharField(default=None, max_length=200, null=True, verbose_name='Url на картинку'),
        ),
    ]