# from django.shortcuts import render

# Create your views here.
from django.db.models.query import QuerySet
from rest_framework import generics ,status,views
from backend import serializers
from django.contrib.auth.models import User
from django.middleware.csrf import get_token
from backend.models import Post

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import permissions

from backend.permissions import IsOwnerOrReadOnly
# from watson import search as watson

class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer

# class UserDetail(generics.RetrieveAPIView):
#     queryset = User.objects.all()
#     serializer_class = serializers.UserSerializer



class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = serializers.PostSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]


    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = serializers.PostSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly,
    #                       IsOwnerOrReadOnly]


class SearchWord(generics.ListAPIView):
    serializer_class = serializers.PostSerializer

    #     # key_word = self.request.query_params.get('term','')
    #     # key_word = self.request.data['term']
   
    def get_queryset(self):
        term = self.kwargs['term']

        querySet = Post.objects.filter(body__icontains=term)

        return querySet
  
   
        
class SearchWordByCount(generics.ListAPIView):
    serializer_class = serializers.PostSerializer
    queryset = Post.objects.all()
  

    def list(self, request, *args, **kwargs):
        term = self.kwargs['word']
        count = self.kwargs['count']
        
        querySet = Post.objects.filter(body__icontains=term)
        if len(querySet) == count:
            serializer = serializers.PostSerializer(querySet,many=True)
            return Response(serializer.data)

        return Response({'msg':'No match for count'},400)


@api_view(['GET'])
def get_csrf_token(request):
    token = get_token(request)
    return Response({'token': token})