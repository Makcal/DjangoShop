from django.db.models import *


class Product(Model):
    name = CharField('Название', max_length=130, default=None)
    desc = TextField('Описание', default=None)
    photo = CharField('Url на картинку', max_length=200, default=None)
    price = DecimalField('Цена', decimal_places=2, max_digits=10)
    amount = PositiveIntegerField('Кол-во')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
