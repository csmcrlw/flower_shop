from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True, verbose_name='Название')
    slug = models.SlugField(max_length=200, db_index=True, unique=True)

    class Meta:
        ordering = ('name', )
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE,
                                 blank=True, null=True, verbose_name='Категория')
    name = models.CharField(max_length=200, db_index=True, unique=True, verbose_name='Название')
    slug = models.SlugField(max_length=200, db_index=True, default='')
    description = models.TextField(blank=True, verbose_name='Описание')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    stock = models.PositiveIntegerField(default=0, verbose_name='Осталось на складе')
    available = models.BooleanField(default=True, verbose_name='Доступно для заказа')

    class Meta:
        ordering = ('name', )
        index_together = (('id', 'slug'), )
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.name

    def is_available(self):
        if self.stock == 0:
            self.available = False
        return self.available
