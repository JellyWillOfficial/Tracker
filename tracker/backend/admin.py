from django.contrib import admin
from .models import (
    CategoriesOfSpending,
    NameOfStores
)


admin.site.register(CategoriesOfSpending)
admin.site.register(NameOfStores)
