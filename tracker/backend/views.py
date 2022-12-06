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
    StoreNamesSerializer,
    SpendingSerializer,
)
from .models import (
    CategoriesOfSpending,
    StoreNames,
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
    fields = []
    def post(self, request):
        dict_for_serializer = {}
        for i in self.fields:
            if i == 'owner':
                dict_for_serializer.update({'owner': request.user.id})
                continue
            if i not in request.data.keys():
                continue
            if i == 'password':
                dict_for_serializer.update({'password': make_password(request.data['password'])})
            elif i == 'is_staff':
                dict_for_serializer.update({'is_staff': self.is_staff})
            elif i == 'is_superuser':
                dict_for_serializer.update({'is_superuser': self.is_superuser})
            else:
                dict_for_serializer.update({i: request.data[i]})
        serializer = self.serializer(data=dict_for_serializer)
        if serializer.is_valid():
            serializer.save()
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
    fields = ['owner', 'name']

class StoreNamesCreateView(CreateView):
    serializer = StoreNamesSerializer
    fields = ['owner', 'name']

class SpendingCreateView(CreateView):
    serializer = SpendingSerializer
    fields = ['owner', 'date', 'name', 'price', 'weight', 'category', 'store', 'significance']

class GetAllCategoriesOfSpendingOfUserView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request):
        lines = CategoriesOfSpending.objects.filter(owner=request.user.id)
        serializer = CategoriesOfSpendingSerializer(lines, many=True)
        return Response(serializer.data)

class GetAllStoreNamesOfUserView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request):
        lines = StoreNames.objects.filter(owner=request.user.id)
        serializer = StoreNamesSerializer(lines, many=True)
        return Response(serializer.data)