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
    http_method_names = ['get', 'update', 'delete',]

    def get_object(self):
        return self.request.user


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [ permissions.IsAdminUser, ]
    authentication_classes = [authentication.TokenAuthentication, authentication.SessionAuthentication]

    

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