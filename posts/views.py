from django.shortcuts import render
from rest_framework.decorators import api_view 
from rest_framework import status

# Set permission for request of methods(permission_classes decorator)
from rest_framework.decorators import permission_classes 
from rest_framework import permissions

from rest_framework.response import Response
from posts.models import Post
from posts.serializers import PostSerializer

@api_view(['GET','POST'])
@permission_classes((permissions.AllowAny,))
def post_list(request, format=None):

    if request.method == 'GET':
        post = Post.objects.all()
        serializer = PostSerializer(post, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
@permission_classes((permissions.AllowAny,))
def post_detail(request, pk, format=None):

    try:
        post = Post.objects.get(pk=pk)
    except Post.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PostSerializer(post)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = PostSerializer(post,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.erros, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
