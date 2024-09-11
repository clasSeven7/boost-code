from rest_framework import routers

from plataforma.api.comment import viewsets

Comment_router = routers.DefaultRouter()
Comment_router.register('', viewsets.CommentViewSet)
