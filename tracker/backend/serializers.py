from django.contrib.auth.models import User, Group
from rest_framework import serializers
from django.contrib.auth.hashers import make_password


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        _groups = Group
        fields = ['url', 'name']

class UserSerializer(serializers.HyperlinkedModelSerializer):
    groups = serializers.PrimaryKeyRelatedField(queryset=Group.objects.all(), many=True)
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'groups', "is_staff", "is_superuser"]
