from rest_framework.permissions import BasePermission

class IsAdmin(BasePermission):
    message = "Siz Admin Emasssiz!"
    
    def has_permission(self, request, view):
        return request.user and request.user.is_admin
    
class IsManager(BasePermission):
    message = "Siz Manager Emassiz!"
    
    def has_permission(self, request, view):
        return request.user and request.user.is_manager
    
class IsUser(BasePermission):
    message = "Siz User Emassiz!"
    
    def has_permission(self, request, view):
        return request.user and request.user.is_user
    
class IsStaff(BasePermission):
    message = 'Siz Staff Emassiz!'
    
    def has_permission(self, request, view):
        return request.user and not (request.user.is_admin or request.user.is_manager)