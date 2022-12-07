from django.contrib.auth.models import User, Group
from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from .models import (
    CategoriesOfSpending,
    StoreNames,
    Spending,
)


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class UserSerializer(serializers.HyperlinkedModelSerializer):
    groups = serializers.PrimaryKeyRelatedField(queryset=Group.objects.all(), many=True)
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'groups', "is_staff", "is_superuser"]

class CategoriesOfSpendingSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoriesOfSpending
        exclude = []

class StoreNamesSerializer(serializers.ModelSerializer):
    class Meta:
        model = StoreNames
        exclude = []

class SpendingSerializer(serializers.ModelSerializer):
    category = CategoriesOfSpendingSerializer(many=False, read_only=True)
    store = StoreNamesSerializer(many=False, read_only=True)
    class Meta:
        model = Spending
        exclude = []
