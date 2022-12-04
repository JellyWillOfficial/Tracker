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
    NameOfStores,
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

class RegistrationView(APIView):
    is_staff = False
    is_superuser = False
    def post(self, request):
        serializer = UserSerializer(
            data=
            {
                'username': request.data['username'], 
                'email': request.data['email'], 
                'password': make_password(request.data['password']), 
                'groups': request.data['groups'],
                'is_staff': self.is_staff,
                'is_superuser': self.is_superuser
            }
        )
        if serializer.is_valid():
            serializer.save()
        else:
            print('is not valid')
        serializer.save()
        return Response(serializer.data)

class RegistrationStaff(RegistrationView):
    permission_classes = [permissions.IsAdminUser]
    is_staff = True
    is_superuser = True

class RegistrationSuperUser(RegistrationView):
    permission_classes = [permissions.IsAdminUser]
    is_superuser = True

class RegistrationUser(RegistrationView):
    pass

class CategoriesOfSpendingCreateView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def post(self, request):
        serializer = CategoriesOfSpendingSerializer(
            data=
            {
                'name': request.data['name'],
                'owner': request.user.id
            }
        )
        if serializer.is_valid():
            serializer.save()
        else:
            print('is not valid')
        serializer.save()
        return Response(serializer.data)


class NameOfStoresCreateView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def post(self, request):
        serializer = NameOfStores(
            data=
            {
                'name': request.data['name'],
                'owner': request.user.id
            }
        )
        if serializer.is_valid():
            serializer.save()
        else:
            print('is not valid')
        serializer.save()
        return Response(serializer.data)
