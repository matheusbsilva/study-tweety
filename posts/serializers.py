from rest_framework import serializers
from posts.models import Post 

class PostSerializer(serializers.Serializer):
    id = serializers.IntergerField(read_only=True)
    text = serializers.CharField(max_length=150)
    likes = serializers.IntegerField(read_only=True)
    owner = serializers.StringRelatedField(many=True)

    def create(self, validated_data):
        return Post.objects.create(validated_Data)

    def update(self, instance, validated_data):
        instance.text = validated_data.get('text', instance.text)
        instance.likes= validated_data.get('likes', instance.likes)
        instance.save()
        return instance

