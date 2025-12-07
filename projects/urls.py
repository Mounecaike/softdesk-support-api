from rest_framework.routers import DefaultRouter

from users.urls import urlpatterns
from .views import ContributorViewSet, ProjectViewSet, IssueViewSet, CommentViewSet

router = DefaultRouter()
router.register(r'projects', ProjectViewSet, basename='projects')
router.register(r'contributors', ContributorViewSet, basename='contributors')
router.register(r'issues', IssueViewSet, basename='issues')
router.register(r'comments', CommentViewSet, basename='comments')

urlpatterns = router.urls