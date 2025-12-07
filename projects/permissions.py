from rest_framework.permissions import BasePermission, SAFE_METHODS
from .models import Contributor

class IsAuthorOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.author == request.user


class IsProjectContributor(BasePermission):
    def has_permission(self, request, view):
        project_id = request.data.get('project') or view.kwargs.get('project_pk')

        if not project_id:
            return True

        return Contributor.objects.filter(
            user=request.user,
            project_id=project_id
        ).exists()

class IsAssigneeOrAuthorOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True

        return obj.author == request.user
