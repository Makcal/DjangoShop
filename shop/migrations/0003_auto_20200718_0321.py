# Generated by Django 3.0.7 on 2020-07-18 00:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_auto_20200718_0313'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='photo',
            field=models.CharField(max_length=200, null=True, verbose_name='Url на картинку'),
        ),
    ]
