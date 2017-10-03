from django.http import Http404

from rest_framework import mixins
from rest_framework import generics 

from posts.models import Post
from posts.serializers import PostSerializer

class PostList(mixins.ListModelMixin,
               mixins.CreateModelMixin,
               generics.GenericAPIView):

    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

    #def get(self, request, format=None):
        #posts = Post.objects.all()
        #serializer = PostSerializer(posts, many=True)
        #return Response(serializer.data)
    
    #def post(self, request, format=None):
        #serializer = PostSerializer(data=request.data)
        #if serializer.is_valid():
            #serializer.save()
            #return Response(serializer.data, status=status.HTTP_201_CREATED)
        #return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    #def delete(self, request, format=None):
        #posts = Post.objects.all()
        #posts.delete()
        #return Response(status=status.HTTP_204_NO_CONTENT)

class PostDetail(mixins.RetrieveModelMixin,
                 mixins.UpdateModelMixin,
                 mixins.DestroyModelMixin,
                 generics.GenericAPIView):

    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get(self, request, *args, **kwargs):
        return self.retrive(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

    #def get_object(self, pk):
        #try:
            #return Post.objects.get(pk=pk)
        #except Post.DoesNotExist:
            #raise Http404

    #def get(self, request, pk, format=None):
        #post = self.get_object(pk)
        #serializer = PostSerializer(post)
        #return Response(serializer.data)

    #def put(self, request, pk, format=None):
        #post = self.get_object(pk)
        #serializer = PostSerializer(post, data=request.data)
        #if serializer.is_valid():
            #serializer.save()
            #return Response(serializer.data)
        #return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    #def delete(self, request, pk, format=None):
        #post = self.get_object(pk)
        #post.delete()
        #return Response(status=status.HTTP_204_NO_CONTENT)
