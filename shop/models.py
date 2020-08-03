from django.db import models
from django.urls import reverse


class Category(models.Model):
    """Категории"""
    name = models.CharField("Категория", max_length=150, db_index=True)
    url = models.SlugField(max_length=160, db_index=True, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Product(models.Model):
    """Товар"""
    category = models.ForeignKey(Category, verbose_name='Товар', on_delete=models.SET_NULL, null=True)
    name = models.CharField("Наименование", max_length=160, db_index=True)
    url = models.SlugField(max_length=160, db_index=True)
    image = models.ImageField("Изображение", upload_to='products/')
    description = models.TextField("Описание", blank=True)
    price = models.DecimalField("Цена", max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField("Количество")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("product_detail", kwargs={'slug': self.url})

    class Meta:
        ordering = ('name',)
        index_together = (('id', 'url'),)
        verbose_name = "Товар"
        verbose_name_plural = "Товары"
