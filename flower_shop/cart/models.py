from django.db import models
from django.contrib.auth import get_user_model

import shop.models


User = get_user_model()


class CustomUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Пользователь')
    first_name = models.CharField(max_length=255, null=False, verbose_name='Имя')
    last_name = models.CharField(max_length=255, null=False, default=None, verbose_name='Фамилия')
    email = models.EmailField(unique=True, default=None, verbose_name='Email')
    phone = models.CharField(max_length=15, unique=True, default=None, verbose_name='Телефон')
    address = models.CharField(max_length=255, default=None, verbose_name='Адрес')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Создано')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Обновлено')

    class Meta:
        verbose_name = "Данные пользователя"
        verbose_name_plural = "Данные пользователей"

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.id}"


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Пользователь')
    products = models.ManyToManyField(shop.models.Product, blank=True, verbose_name='Товары')
    quantity = models.IntegerField(null=False, default=0, verbose_name='Количество')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Создано')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Обновлено')
    is_ordered = models.BooleanField(verbose_name='Заказано', default=False)
    is_delivered = models.BooleanField(verbose_name='Доставлено', default=False)

    class Meta:
        verbose_name = "Корзина"
        verbose_name_plural = "Корзины"

    def __str__(self):
        return f"{self.user} - {self.created_at}"
