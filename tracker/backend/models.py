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

class NameOfStores(models.Model):
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
