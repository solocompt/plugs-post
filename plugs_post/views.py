from rest_framework import viewsets
from rest_framework import permissions

from plugs_post import models
from plugs_post import serializers


class PostViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Post Viewset
    """
    queryset = models.Post.objects.all()
    serializer_class = serializers.PostSerializer
    permission_classes = [permissions.AllowAny]
    lookup_field = 'slug'


class PostSectionViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Post Section Viewset
    """
    queryset = models.PostSection.objects.all()
    serializer_class = serializers.PostSectionSerializer
    permission_classes = [permissions.AllowAny]
    lookup_field = 'slug'
