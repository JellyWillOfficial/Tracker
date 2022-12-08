from django.urls import include, path
from rest_framework import routers
from .views import UserViewSet, GroupViewSet
from .views import (
    RegistrationStaff,
    RegistrationSuperUser,
    RegistrationUser,
    CategoriesOfSpendingCreateView,
    StoreNamesCreateView,
    SpendingCreateView,
    GetAllCategoriesOfSpendingOfUserView,
    GetAllStoreNamesOfUserView,
    GetAllSpendingOfUserView,
    CategoryOfSpendingPutView,
    CategoryOfSpendingDeleteView,
)

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('api/auth/', include('djoser.urls')),
    path('api/registrarion/staff/',RegistrationStaff.as_view()),
    path('api/registrarion/superuser/',RegistrationSuperUser.as_view()),
    path('api/registrarion/user/',RegistrationUser.as_view()),
    path('api/categories-of-spending/create/', CategoriesOfSpendingCreateView.as_view()),
    path('api/store-names/create/', StoreNamesCreateView.as_view()),
    path('api/spending/create/', SpendingCreateView.as_view()),
    path('api/categories-of-spending/display/categories/all/', GetAllCategoriesOfSpendingOfUserView.as_view()),
    path('api/store-names/display/stores/all/', GetAllStoreNamesOfUserView.as_view()),
    path('api/spending/display/spending/all/', GetAllSpendingOfUserView.as_view()),
    path('api/categories-of-spending/update/categories/<int:pk>/', CategoryOfSpendingPutView.as_view()),
    path('api/categories-of-spending/delete/categories/<int:pk>/', CategoryOfSpendingDeleteView.as_view()),
    path('', include(router.urls)),
]
