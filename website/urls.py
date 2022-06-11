from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from club import views
from club import views


router = DefaultRouter()

router.register('category', views.CategoryViewSet, basename='category')
router.register('group', views.GroupViewSet, basename='group')
router.register('profile', views.UserProfile, basename='profile')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-token-auth/', obtain_auth_token),
    path('auth/', include('rest_framework.urls')),
    path('create-admin/', views.AdminUserCreateAPIView.as_view()),
    path('create/', views.UserCreateView.as_view()),
    path('', include(router.urls)),
]