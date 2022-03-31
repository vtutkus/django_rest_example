from django.urls import path, include
from .views import PostList, PostDetail, CommentList, CommentDetail, PostLikeCreate, UserCreate, CommentLikeCreate, UserList, UserDetail

urlpatterns = [
    path('posts', PostList.as_view()),
    path('posts/<int:pk>', PostDetail.as_view()),
    path('posts/<int:pk>/comments', CommentList.as_view()),
    path('comments/<int:pk>', CommentDetail.as_view()),
    path('comments/<int:pk>/like', CommentLikeCreate.as_view()),
    path('posts/<int:pk>/like', PostLikeCreate.as_view()),
    path('comments/<int:pk>/like', CommentLikeCreate.as_view()),
    path('signup', UserCreate.as_view()),
    path('users', UserList.as_view()),
    path('users/<int:pk>', UserDetail.as_view()),
]
