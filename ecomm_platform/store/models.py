from django.db import models
from django.core.validators import RegexValidator


# Create your models here.
class ArticleField(models.CharField):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # 3 letters in areas [A-I][J-R][S-Z], 4 nulls, 3 any digits
        self.validators.append(RegexValidator(regex=r'^[A-I]{1}[J-R]{1}[S-Z]{1}0{4}\d{3}$'))


class Good(models.Model):
    TYPE_CHOICES = [
        ('Комплектующие ПК', (
            ('cpu', 'CPU'),
            ('motherboard', 'материнская плата'),
            ('gpu', 'GPU'),
            ('ram', 'RAM'),
        )
         ),
        ('Периферийные устройства', (
            ('mouse', 'мышь'),
            ('keyboard', 'клавиатура'),
        )
         ),
        ('Остальное', (
            ('ties', 'кабельные стяжки'),
        )
         ),
    ]
    article_num = ArticleField(max_length=10)
    name = models.CharField(max_length=50)
    price = models.PositiveIntegerField()
    type = models.CharField(max_length=30, choices=TYPE_CHOICES)
