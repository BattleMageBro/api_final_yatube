from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import PostViewSet, CommentViewSet, FollowView, GroupView


urlpatterns = [
    path('posts/', PostViewSet.as_view(actions={'get': 'list', 'post': 'create'})),
    path('posts/<int:pk>/', PostViewSet.as_view(actions={'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'})),
    path('posts/<int:post_pk>/comments/', CommentViewSet.as_view(actions={'get': 'list', 'post': 'create'})),
    path('posts/<int:post_pk>/comments/<int:pk>/', CommentViewSet.as_view(actions={'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'})),
    path('follow/', FollowView.as_view()),
    path('group/', GroupView.as_view()),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
