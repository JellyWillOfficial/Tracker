from django.db import models
from django.contrib.auth import get_user_model


class CategoriesOfSpending(models.Model):
    """
    Категории расходов, модель для категоризации статей расходов пользователя
    """
    name = models.CharField(max_length=50)
    owner = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE)
    
    def __str__(self):
        return '{}'.format(self.name)
    
    class Meta:
        verbose_name = 'Категория расходов'
        verbose_name_plural = 'Категории расходов'

class StoreNames(models.Model):
    """
    Название магазинов, модель для отслеживания магазина где была произведена трата средств
    """
    name = models.CharField(max_length=50)
    owner = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE)
    
    def __str__(self):
        return '{}'.format(self.name)
    
    class Meta:
        verbose_name = 'Название магазина'
        verbose_name_plural = 'Названия магазинов'

class Spending(models.Model):
    """
    Расходы, основная модель для подсчёта расходов
    """
    DEGREES = (
        ('V', 'Very important'),
        ('I', 'Important'),
        ('N', 'Not important'),
    )
    owner = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE)
    date = models.DateField()
    name = models.CharField(max_length=50)
    price = models.FloatField()
    weight = models.FloatField(blank=True, null=True, default=None)
    category = models.ForeignKey(
        CategoriesOfSpending, on_delete=models.SET_NULL, blank=True, null=True, default=None
    )
    store = models.ForeignKey(
        StoreNames, on_delete=models.SET_NULL, blank=True, null=True, default=None
    )
    significance = models.CharField(max_length=1, choices=DEGREES)

    def __str__(self):
        return '{} - {} - {}'.format(self.name, self.date, self.price)

    class Meta:
        verbose_name = 'Расходы'
        verbose_name_plural = 'Расходы'
