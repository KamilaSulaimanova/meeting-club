from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model


class User(AbstractUser):
    REQUIRED_FIELDS = ['password', 'full_name',]
    USERNAME_FIELD = 'email'
    username = None
    email = models.EmailField(blank=False, null=False, unique=True)
    full_name = models.CharField(max_length=250, )
    instagram = models.URLField(max_length=250, null=True, blank=True)
    telegram = models.URLField(max_length=250, null=True, blank=True)
    facebook = models.URLField(max_length=250, null=True, blank=True)
    photo = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.full_name


class Category(models.Model):
    name = models.CharField(max_length=250)
    image = models.ImageField()

    def __str__(self):
        return self.name


class Group(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    image = models.ImageField()
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Post(models.Model):
    text = models.CharField(max_length=255)
    publication_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.CharField(max_length=255)

    def __str__(self):
        return self.text


class Like(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.post

