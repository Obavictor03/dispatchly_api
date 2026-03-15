from rest_framework.permissions import BasePermission

class IsSender(BasePermission):
    def has_permission(self, request, view):
        return (
            request.user.is_authenticated 
            and request.user.role == 'sender'
        )
    

class IsRider(BasePermission):
    def has_permission(self, request, view):
        return (
            request.user.is_authenticated 
            and request.user.role == 'rider'
        )
    