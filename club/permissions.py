from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsSafeIsAuthenticated(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS and request.user.is_authenticated:
            return True
        

