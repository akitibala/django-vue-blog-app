# from django.shortcuts import render

# Create your views here.
from django.db.models.query import QuerySet
from django.db.models.query_utils import Q
from rest_framework import generics ,status,views
from rest_framework.serializers import Serializer
from backend import serializers
from django.contrib.auth.models import User
from django.middleware.csrf import get_token
from backend.models import Post
from django.contrib.auth import authenticate


from rest_framework.decorators import api_view
from rest_framework.response import Response
# from rest_framework import permissions
from rest_framework.permissions import AllowAny
# from backend.permissions import IsOwnerOrReadOnly

class UserIdAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer
    permission_classes = (AllowAny,)
    

    def create(self, request, *args, **kwargs):
    
        username = self.request.data['username']
        password = self.request.data['password']
        # user = authenticate(request, username=username, password=password)
        user = User.objects.filter(username=username,password=password)
        if user is  None:
            return Response({'msg':'Enter correct Credentials'},400)
            
        else:
            # print(user)
            serializer = serializers.UserSerializer(user,many=True)
            return Response(serializer.data)

class UserCreateAPIView(generics.CreateAPIView):
    serializer_class = serializers.UserSerializer
    queryset = User.objects.all()
    permission_classes = (AllowAny,)


class PostList(generics.CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = serializers.PostSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]


    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class PostDetail(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = serializers.PostSerializer

    def list(self, request, *args, **kwargs):

       
        name = self.kwargs['owner']
        posts = Post.objects.filter(owner=name)
        # print(name)
        serializer= serializers.PostSerializer(posts,many=True)
        print(serializer.data)
        return Response(serializer.data)

    # permission_classes = [permissions.IsAuthenticatedOrReadOnly,
    #                       IsOwnerOrReadOnly]


class SearchWord(generics.ListAPIView):
    serializer_class = serializers.PostSerializer

    #     # key_word = self.request.query_params.get('term','')
    #     # key_word = self.request.data['term']
   
    def get_queryset(self):
        term = self.kwargs['term']
        print(term)

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