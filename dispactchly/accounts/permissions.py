from rest_framework.permissions import BasePermission

class IsSender(BasePermission):
    def has_permission(self, request, view):
        return (
            request.user_is_authenticated 
            and hasattr(request.user, 'sender')
            and request.user.role == 'sender'
        )
    

class IsRider(BasePermission):
    def has_permission(self, request, view):
        return (
            request.user_is_authenticated 
            and hasattr(request.user, 'rider')
            and request.user.role == 'rider'
        )
    