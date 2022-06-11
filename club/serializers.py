from rest_framework import serializers
from .models import Category, Group, User


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'
        read_only_fields = ['user', 'date_created',]


class AdminUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'password']

    def create(self, validated_data):
        admin = User(
            email=validated_data['email'],
        )
        admin.set_password(validated_data['password'])
        admin.is_staff = True
        admin.is_superuser = True
        admin.save()
        return admin


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'password', 'full_name', 'instagram', 'facebook', 'telegram']

    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
        )
        user.set_password(validated_data['password'])
        user.save() 
        return user
