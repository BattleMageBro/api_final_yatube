from django.shortcuts import get_object_or_404
from rest_framework import viewsets, generics, filters
from .models import Post, Comment, Follow, Group
from . import serializers
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import permissions
from .permissions import IsAuthorOrReadOnly


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = serializers.PostSerializer
    permission_classes = [IsAuthorOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['group',]

    def perform_create(self, serializer): 
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = serializers.CommentSerializer
    permission_classes = [IsAuthorOrReadOnly,]

    def perform_create(self, serializer):
        post = get_object_or_404(Post, pk=self.kwargs.get('post_pk'))
        serializer.save(author=self.request.user, post=post)

    def get_queryset(self):
        post = get_object_or_404(Post, pk=self.kwargs.get('post_pk'))
        return post.comments


class FollowView(generics.ListCreateAPIView):
    queryset = Follow.objects.all()
    serializer_class = serializers.FollowSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,]
    filter_backends = [filters.SearchFilter,]
    search_fields = ['=user__username', '=following__username',]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class GroupView(generics.ListCreateAPIView):
    queryset = Group.objects.all()
    serializer_class = serializers.GroupSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,]
