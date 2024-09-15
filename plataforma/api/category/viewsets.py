import logging

from rest_framework import permissions, viewsets

from plataforma import models
from plataforma.api.category import serializers

logger = logging.getLogger('custom')


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        logger.info(f'Novo {self.request.data["name"]}')
        serializer.save()
