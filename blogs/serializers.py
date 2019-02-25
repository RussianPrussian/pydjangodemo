from django.contrib.auth.models import User, Group
from rest_framework import serializers

from blogs.models import Post


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')


class PostSerializer(serializers.Serializer):
    post_text = serializers.CharField(required=True)
    author = serializers.CharField(required=False)
    pub_date = serializers.DateTimeField()

    def create(self, validated_data):
        return Post.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.post_text = validated_data.get('post_text', instance.post_text)
        instance.author = validated_data.get('author', instance.author)
        instance.pub_date = validated_data.get('pub_date', instance.pub_date)
        instance.save()
        return instance

