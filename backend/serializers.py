from django.contrib.auth import models
from rest_framework import fields, serializers
from django.contrib.auth.models import User
from backend.models import Post

class PostSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Post
        fields = ['id', 'body', 'owner']





class UserSerializer(serializers.ModelSerializer):
    posts = serializers.PrimaryKeyRelatedField(many=True,read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'posts','password']

    def create(self, validated_data):
        user = super(UserSerializer, self).create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user


