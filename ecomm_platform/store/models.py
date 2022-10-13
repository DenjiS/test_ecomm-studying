from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation

from django.core.validators import RegexValidator, MinValueValidator


class Image(models.Model):
    image = models.ImageField(upload_to='static/img')
    default = models.BooleanField(default=False)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    def save(self, **kwargs):
        if self.default:
            Image.objects.filter(content_type=self.content_type, object_id=self.object_id).update(default=False)
        super().save(**kwargs)


class Tag(models.Model):
    word = models.CharField(max_length=63)
    url = models.URLField(blank=True)

    def __str__(self):
        return self.word


class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(default=None)
    images = GenericRelation(Image)

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name


class Product(models.Model):
    article_name = models.SlugField(
        max_length=10,
        validators=[RegexValidator(regex=r'^[A-I]{1}[J-R]{1}[S-Z]{1}0{4}\d{3}$'), ],
        unique=True
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(limit_value=0.99), ]
    )
    name = models.CharField(max_length=255)
    description = models.TextField(default=None)
    images = GenericRelation(Image)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    tags = models.ManyToManyField(Tag, related_name='products')
    rating = models.PositiveIntegerField(default=0, editable=False)
    hot = models.BooleanField(default=False, editable=False)
    new = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    def sold(self):
        self.rating += 1
        self.hot = True if self.rating >= 1000 else False


class Promo(models.Model):
    name = models.CharField(max_length=255)
    active = models.BooleanField(default=True)
    url = models.URLField(blank=True)

    slider_width, slider_height = 800, 400
    slider_image = models.ImageField(upload_to='static/img', width_field='slider_width', height_field='slider_height')
    images = GenericRelation(Image)

    header = models.CharField(max_length=31)
    short_text = models.CharField(max_length=127)
    text = models.TextField(blank=True)

    def __str__(self):
        return self.name
