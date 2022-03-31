from django.conf import settings
from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Post, Comment, PostLike, CommentLike


class UserPasswordSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'first_name', 'last_name', 'email']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user
    
    def update(self, instance, validated_data):
        password = validated_data.pop('password')
        instance.username = validated_data.pop('username')
        instance.set_password(password) 
        instance.save()
        return instance


class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email']


class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email']


class CommentSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    user_id = serializers.ReadOnlyField(source='user.id')
    post = serializers.ReadOnlyField(source='post.id')
    likes_count = serializers.SerializerMethodField()

    def get_likes_count(self, obj):
        return CommentLike.objects.filter(comment=obj).count()   

    class Meta:
        model = Comment
        fields = ['id', 'user', 'user_id', 'post',
                  'body', 'created_at', 'likes_count']


class PostSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    user_id = serializers.ReadOnlyField(source='user.id')
    comments = serializers.StringRelatedField(many=True)
    comment_count = serializers.SerializerMethodField()
    likes_count = serializers.SerializerMethodField()

    def get_comment_count(self, obj):
        return Comment.objects.filter(post=obj).count()

    def get_likes_count(self, obj):
        return PostLike.objects.filter(post=obj).count()

    class Meta:
        model = Post
        fields = ['id', 'user', 'user_id', 'title', 'body', 'image',
                  'created_at', 'comments', 'comment_count', 'likes_count']


class PostLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostLike
        fields = ['id']


class CommentLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentLike
        fields = ['id']
