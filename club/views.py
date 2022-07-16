import re
from sre_constants import SUCCESS
from django.shortcuts import get_object_or_404, redirect
from django.core.mail import send_mail
from django.conf import settings
from .models import User, Category, Group, Post, Comment, Like
from rest_framework.viewsets import ModelViewSet
from . import serializers
from rest_framework import authentication, permissions
from .permissions import IsSafeIsAuthenticated, IsAuthorIsAdmin
from rest_framework.generics import CreateAPIView
from rest_framework.authtoken.views import ObtainAuthToken
import os
import math
import random
import smtplib


class CustomObtainAuthToken(ObtainAuthToken):
    serializer_class = serializers.AuthTokenSerializer


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = serializers.CategorySerializer
    authentication_classes = [authentication.TokenAuthentication, authentication.SessionAuthentication]
    permission_classes = [IsSafeIsAuthenticated,]


class GroupViewSet(ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = serializers.GroupSerializer
    authentication_classes = [authentication.TokenAuthentication, authentication.SessionAuthentication]
    permission_classes = [IsSafeIsAuthenticated, ]

    def get_queryset(self):
        queryset = self.queryset
        category = self.request.GET.get('category')
        if category:
            category = Category.objects.filter(name__icontains=category)
            category_id = []
            for c in category:
                category_id.append(c.id)
            queryset = queryset.filter(category_id__in=category_id)
        return queryset

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class AdminUserCreateAPIView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.AdminUserSerializer


class UserCreateView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer

    def perform_create(self, serializer):
        user = serializer.save()
        digits = "0123456789abcdefghijklmnopqrstuvwxyz"
        otp = ''
        for i in range(6):
            otp += digits[math.floor(random.random() * 10)]
        user.otp = otp
        subject = 'Your account verification email'
        msg = user.otp + " is your OTP"
        email_from = settings.EMAIL_HOST_USER
        send_mail(subject, msg, email_from, [user.email])
    


def verify_otp(request):
    otp = request.GET.get('otp')
    if otp == request.user.otp:
        request.user.is_verified = True
        print("Verified")
    else:
        print("Please Check your OTP again")
    

class UserProfile(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = serializers.UserProfileSerializer
    http_method_names = ['get', 'put', 'delete', ]
    authentication_classes = [authentication.TokenAuthentication, authentication.SessionAuthentication]

    def get_object(self):
        return self.request.user


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = serializers.PostSerializer
    permission_classes = [IsSafeIsAuthenticated, ]
    authentication_classes = [authentication.TokenAuthentication, authentication.SessionAuthentication]

    def get_queryset(self):
        user = self.request.user
        groups = Group.objects.filter(user=user)
        posts = Post.objects.filter(group__in=groups)
        return posts


class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = serializers.CommentSerializer
    permission_classes = [IsAuthorIsAdmin, ]
    authentication_classes = [authentication.TokenAuthentication, authentication.SessionAuthentication]

    def get_queryset(self):
        user = self.request.user
        groups = Group.objects.filter(user=user)
        posts = Post.objects.filter(group__in=groups)
        comments = Comment.objects.filter(post__in=posts)
        return comments
        
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class LikeViewSet(ModelViewSet):
    queryset = Like.objects.all()
    serializer_class = serializers.LikeSerializer
    permission_classes = [IsAuthorIsAdmin, ]
    authentication_classes = [authentication.TokenAuthentication, authentication.SessionAuthentication]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
