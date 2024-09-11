from rest_framework import viewsets

from plataforma import models
from plataforma.api.comment import serializers


class CommentViewSet(viewsets.ModelViewSet):
    queryset = models.Comment.objects.all()
    serializer_class = serializers.CommentSerializer
