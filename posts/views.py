from django.http import Http404

from rest_framework import mixins
from rest_framework import generics 

from posts.models import Post
from posts.serializers import PostSerializer

class PostList(generics.ListCreateAPIView):

    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset = Post.objects.all()
    serializer_class = PostSerializer

