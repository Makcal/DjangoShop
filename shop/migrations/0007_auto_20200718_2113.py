# Generated by Django 3.0.8 on 2020-07-18 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_auto_20200718_2111'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='photo',
            field=models.CharField(default='null', max_length=200, null=True, verbose_name='Url на картинку'),
        ),
    ]
