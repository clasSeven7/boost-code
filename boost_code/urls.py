from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from plataforma.api.category.router import Category_router
from plataforma.api.comment.router import Comment_router
from plataforma.api.post.router import Post_router

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/post/', include(Post_router.urls)),
    path('api/category/', include(Category_router.urls)),
    path('api/comment/', include(Comment_router.urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
