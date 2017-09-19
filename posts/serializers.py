from rest_framework import serializers
from posts.models import Post 

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id','text','likes','owner')

    def create(self, validated_data):
        return Post.objects.create(validated_data)

    def update(self, instance, validated_data):
        instance.text = validated_data.get('text', instance.text)
        instance.likes= validated_data.get('likes', instance.likes)
        instance.save()
        return instance

    class Meta:
        model = Post
        fields = ('text','likes','owner')

