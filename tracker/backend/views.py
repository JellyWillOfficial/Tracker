from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.views import APIView
from django.contrib.auth.hashers import make_password
from rest_framework.response import Response
from .serializers import (
    UserSerializer, 
    GroupSerializer,
    CategoriesOfSpendingSerializer,
    NameOfStoresSerializer,
    SpendingSerializer,
    )


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

class CreateView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer = None
    owner_exists = False
    fields = []
    def post(self, request):
        dict_for_serializer = {}
        for i in self.fields:
            if i == 'password':
                dict_for_serializer.update({'password': make_password(request.data['password'])})
            elif i == 'is_staff':
                dict_for_serializer.update({'is_staff': self.is_staff})
            elif i == 'is_superuser':
                dict_for_serializer.update({'is_superuser': self.is_superuser})
            else:
                dict_for_serializer.update({i: request.data[i]})
        if self.owner_exists:
            dict_for_serializer.update({'owner': request.user.id})
        serializer = self.serializer(data=dict_for_serializer)
        if serializer.is_valid():
            serializer.save()
        else:
            print('is not valid')
        serializer.save()
        return Response(serializer.data)

class RegistrationView(CreateView):
    is_staff = False
    is_superuser = False
    serializer = UserSerializer
    fields = ['username', 'email', 'password', 'groups', 'is_staff', 'is_superuser']

class RegistrationStaff(RegistrationView):
    permission_classes = [permissions.IsAdminUser]
    is_staff = True
    is_superuser = True

class RegistrationSuperUser(RegistrationView):
    permission_classes = [permissions.IsAdminUser]
    is_superuser = True

class RegistrationUser(RegistrationView):
    pass

class CategoriesOfSpendingCreateView(CreateView):
    serializer = CategoriesOfSpendingSerializer
    owner_exists = True
    fields = ['name']

class NameOfStoresCreateView(CreateView):
    serializer = NameOfStoresSerializer
    owner_exists = True
    fields = ['name']

class SpendingCreateView(CreateView):
    serializer = SpendingSerializer
    owner_exists = True
    fields = ['date', 'name', 'price', 'weight', 'category', 'store', 'significance']
