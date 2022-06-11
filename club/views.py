from unicodedata import category

from django.shortcuts import get_object_or_404
from .models import *
from rest_framework.viewsets import ModelViewSet
from .serializers import *
from rest_framework import authentication, permissions
from .permissions import *
from rest_framework.generics import CreateAPIView, RetrieveAPIView
from .serializers import AdminUserSerializer, UserSerializer
from rest_framework import authentication, permissions


User = get_user_model()


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
    http_method_names = ['get', 'put', 'delete',]
    authentication_classes = [authentication.TokenAuthentication, authentication.SessionAuthentication]

    def get_object(self):
        return self.request.user


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsSafeIsAuthenticated, ]
    authentication_classes = [authentication.TokenAuthentication, authentication.SessionAuthentication]


    # def get_queryset(self):
    #     user = self.request.user
    #     for p in self.queryset.iterator():
    #         if 
    #     return Post.objects.filter(group_id__in=user.groups.id)

    

class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthorIsAdmin, ]
    authentication_classes = [authentication.TokenAuthentication, authentication.SessionAuthentication]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class LikeViewSet(ModelViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    permission_classes = [IsAuthorIsAdmin, ]
    authentication_classes = [authentication.TokenAuthentication, authentication.SessionAuthentication]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


def search(request):
    category_id = get_object_or_404(Category, id=id)
    queryset = Group.objects.filter(category=category_id)