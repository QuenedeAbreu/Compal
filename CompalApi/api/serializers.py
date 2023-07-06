from django.contrib.auth.models import User, Group, Permission
from rest_framework import serializers


class PermissionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Permission
        fields = ['id', 'name', 'content_type_id', 'codename']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    permissions = PermissionSerializer(read_only=True, many=True)

    class Meta:
        model = Group
        fields = ['id', 'name', 'permissions']


class GroupSerializer_Edit(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['id', 'name']


class UserSerializer(serializers.HyperlinkedModelSerializer):
    groups = GroupSerializer_Edit(read_only=True, many=True)

    class Meta:
        model = User
        fields = ['id', 'url', 'username', 'email',
                  'first_name', 'last_name',
                  'is_superuser', 'is_active', 'is_staff', 'groups']
