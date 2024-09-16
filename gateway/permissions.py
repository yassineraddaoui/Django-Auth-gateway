from rest_framework.permissions import BasePermission

# Custom permission to check if the user is a recruiter
class IsRecruiter(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.groups.filter(name='recruiter').exists()

# Custom permission to check if the user is a candidate
class IsCandidate(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.groups.filter(name='candidate').exists()
class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.groups.filter(name='admin').exists()
