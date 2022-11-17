from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation

from django.core.validators import RegexValidator, MinValueValidator


class Image(models.Model):
    image = models.ImageField(upload_to='upload/')
    default = models.BooleanField(default=False)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    def save(self, **kwargs):
        if self.default:
            Image.objects.filter(content_type=self.content_type, object_id=self.object_id).update(default=False)
        super().save(**kwargs)


class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)

    description = models.TextField(default=None)
    images = GenericRelation(Image)

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)

    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(limit_value=0.99), ]
    )
    description = models.TextField(default=None)
    images = GenericRelation(Image)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    rating = models.PositiveIntegerField(default=0, editable=False)
    hot = models.BooleanField(default=False, editable=False)
    new = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    def rating_up(self):
        self.rating += 1
        self.hot = True if self.rating >= 1000 else False


class Promo(models.Model):
    name = models.CharField(max_length=255)
    active = models.BooleanField(default=True)
    url = models.URLField(blank=True)

    slider_width, slider_height = 800, 400
    slider_image = models.ImageField(
        upload_to='upload/',
        width_field='slider_width',
        height_field='slider_height'
    )
    images = GenericRelation(Image)

    header = models.CharField(max_length=31)
    short_text = models.CharField(max_length=127)
    text = models.TextField(blank=True)

    def __str__(self):
        return self.name
