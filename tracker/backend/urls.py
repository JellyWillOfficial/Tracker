from django.urls import include, path
from rest_framework import routers
from .views import UserViewSet, GroupViewSet
from .views import RegistrationStaff, RegistrationSuperUser, RegistrationUser

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    #path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('auth/', include('djoser.urls')),
    path('registrarion/staff/',RegistrationStaff.as_view()),
    path('registrarion/superuser/',RegistrationSuperUser.as_view()),
    path('registrarion/user/',RegistrationUser.as_view()),
    path('', include(router.urls)),
]
