from rest_framework import routers

from plataforma.api.post import viewsets

Post_router = routers.DefaultRouter()
Post_router.register('', viewsets.PostViewSet)
