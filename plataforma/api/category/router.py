from rest_framework import routers

from plataforma.api.category import viewsets

Category_router = routers.DefaultRouter()
Category_router.register('', viewsets.CategoryViewSet)
