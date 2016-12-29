from rest_framework import serializers

from plugs_post.models import Post, PostSection

class PostSerializer(serializers.ModelSerializer):
    """
    Post Serializer
    """
    class Meta:
        """
        Metaclass definition
        """
        model = Post
        fields = ('id', 'name', 'text', 'section', 'slug', 'created', 'updated')
        read_only_fields = ('slug', )

class PostSectionSerializer(serializers.ModelSerializer):
    """
    Post Section Serializer
    """
    class Meta:
        """
        Metaclass definition
        """
        model = PostSection
        fields = ('id', 'name', 'description', 'slug', 'created', 'updated')
