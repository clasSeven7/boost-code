import logging

from rest_framework import permissions, viewsets

from plataforma import models
from plataforma.api.comment import serializers

logger = logging.getLogger('custom')


class CommentViewSet(viewsets.ModelViewSet):
    queryset = models.Comment.objects.all()
    serializer_class = serializers.CommentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        logger.info(f'Novo {self.request.data["post"]}')
        serializer.save()
