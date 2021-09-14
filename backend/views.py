# from django.shortcuts import render

# Create your views here.
from django.db.models.query import QuerySet
from rest_framework import generics ,status
from backend import serializers
from django.contrib.auth.models import User
from backend.models import Post

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import permissions

from backend.permissions import IsOwnerOrReadOnly
# from watson import search as watson

# class UserList(generics.ListAPIView):
#     queryset = User.objects.all()
#     serializer_class = serializers.UserSerializer

# class UserDetail(generics.RetrieveAPIView):
#     queryset = User.objects.all()
#     serializer_class = serializers.UserSerializer



class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = serializers.PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = serializers.PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]


class SearchList(generics.ListAPIView):
    serializer_class = serializers.PostSerializer
    http_method_names = ['get']
    def get_queryset(self):
        key_word = self.request.query_params.get('term','')
        queryset = Post.objects.all()
        if key_word:
            queryset = queryset.filter(body__iconatins=key_word)
        return queryset

  
    # def list(self, request):
    #     # Note the use of `get_queryset()` instead of `self.queryset`
    #     # key_word = self.request.query_params.get('term')
    #     word_count = self.request.query_params.get('word-count',None)

    #     if word_count:
    #         pass
    #     results = serializers.PostSerializer(querset)


       


    #     return Response(results)
        


