from rest_framework.permissions import BasePermission

class IsAdminEmail(BasePermission):
    def has_permission(self, request, view):
        return request.user 
        # return request.user and request.user.email == "admin@admin.com"