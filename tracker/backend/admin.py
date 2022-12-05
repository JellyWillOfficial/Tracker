from django.contrib import admin
from .models import (
    CategoriesOfSpending,
    StoreNames,
    Spending,
)


admin.site.register(CategoriesOfSpending)
admin.site.register(StoreNames)
admin.site.register(Spending)
