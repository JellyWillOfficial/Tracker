from django.contrib import admin
from .models import (
    CategoriesOfSpending,
    NameOfStores,
    Spending,
)


admin.site.register(CategoriesOfSpending)
admin.site.register(NameOfStores)
admin.site.register(Spending)
