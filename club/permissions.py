from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsSafeIsAuthenticated(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated and request.method in SAFE_METHODS:
            return True


class IsAuthorIsAdmin(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return True

    def has_object_permission(self, request, view, obj):    
        if request.user.is_staff or request.user.is_authenticated and request.method in SAFE_METHODS :
            return True
        return obj.user == request.user

