from rest_framework import viewsets

from plataforma import models
from plataforma.api.post import serializers


class PostViewSet(viewsets.ModelViewSet):
    queryset = models.Post.objects.all()
    serializer_class = serializers.PostSerializer
