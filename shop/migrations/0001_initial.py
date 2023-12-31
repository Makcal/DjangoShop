# Generated by Django 3.0.7 on 2020-07-18 00:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Название')),
                ('text', models.TextField(verbose_name='Описание')),
                ('photo', models.CharField(max_length=200, verbose_name='Url на картинку')),
                ('price', models.IntegerField(verbose_name='Цена', )),
                ('amount', models.IntegerField(verbose_name='Кол-во')),
            ],
        ),
    ]
