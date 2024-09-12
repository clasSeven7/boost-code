from rest_framework import permissions, viewsets

from plataforma import models
from plataforma.api.category import serializers


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer
    permission_classes = [permissions.IsAuthenticated]
