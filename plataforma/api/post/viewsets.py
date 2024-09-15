import logging

from rest_framework import permissions, viewsets

from plataforma import models
from plataforma.api.post import serializers

logger = logging.getLogger('custom')


class PostViewSet(viewsets.ModelViewSet):
    queryset = models.Post.objects.all()
    serializer_class = serializers.PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        logger.info(f'Novo {self.request.data["title"]}')
        serializer.save()
