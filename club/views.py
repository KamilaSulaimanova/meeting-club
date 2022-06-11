from .models import *
from rest_framework.viewsets import ModelViewSet
from .serializers import CategorySerializer, GroupSerializer
from rest_framework import authentication, permissions
from .permissions import IsSafeIsAuthenticated
from .models import User
from rest_framework.generics import CreateAPIView, RetrieveAPIView
from .serializers import AdminUserSerializer, UserSerializer
from rest_framework import authentication, permissions


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    authentication_classes = [authentication.TokenAuthentication, authentication.SessionAuthentication]
    permission_classes = [IsSafeIsAuthenticated, permissions.IsAdminUser]


class GroupViewSet(ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    authentication_classes = [authentication.TokenAuthentication, authentication.SessionAuthentication]
    permission_classes = [IsSafeIsAuthenticated, permissions.IsAdminUser ]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class AdminUserCreateAPIView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = AdminUserSerializer


class UserCreateView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserProfile(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    http_method_names = ['get', 'update', 'delete',]

    def get_object(self):
        return self.request.user