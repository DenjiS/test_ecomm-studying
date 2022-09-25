from django.db import models
from django.core.validators import RegexValidator, MinValueValidator


def get_upload_path(instance, filename):
    if hasattr(instance, 'cat_model'):
        return f'images/cat/{instance.album.cat_model.name}/{filename}'
    elif hasattr(instance, 'prod_model'):
        return f'images/prod/{instance.album.prod_model.name}/{filename}'


class ImageAlbum(models.Model):
    def default(self):
        return self.images.filter(default=True).first()


class Image(models.Model):
    image = models.ImageField(upload_to=get_upload_path)
    default = models.BooleanField(default=False)
    album = models.ForeignKey(ImageAlbum, on_delete=models.CASCADE, related_name='images')


class Tag(models.Model):
    word = models.CharField(max_length=63)
    url = models.URLField(default=None)


class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(default=None)
    album = models.OneToOneField(ImageAlbum, on_delete=models.CASCADE, related_name='model_cat')

    class Meta:
        verbose_name_plural = 'categories'


class Product(models.Model):
    article_name = models.CharField(
        max_length=10,
        validators=[RegexValidator(regex=r'^[A-I]{1}[J-R]{1}[S-Z]{1}0{4}\d{3}$'), ]
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(limit_value=0.99), ]
    )
    name = models.CharField(max_length=255)
    description = models.TextField(default=None)
    album = models.OneToOneField(ImageAlbum, on_delete=models.CASCADE, related_name='prod_model')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, related_name='products')
