from django.shortcuts import render
from rest_framework import generics, permissions
from .models import Post, Comment, PostLike, CommentLike
from .serializers import PostSerializer


class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        return super().perform_create(serializer)


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    pass