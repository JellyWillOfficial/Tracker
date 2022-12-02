from django.urls import include, path
from rest_framework import routers
from .views import UserViewSet, GroupViewSet
from .views import (
    RegistrationStaff,
    RegistrationSuperUser,
    RegistrationUser,
    CategoriesOfSpendingCreateView,
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
    path('api/create/category-of-spending/', CategoriesOfSpendingCreateView.as_view()),
    path('', include(router.urls)),
]
