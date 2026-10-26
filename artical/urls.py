
from django.urls import path

from .views import (
    ArticleCreateAPIView,
    ArticleListAPIView,
)

urlpatterns = [
    path(
        "articles/",
        ArticleListAPIView.as_view(),
        name="article-list",
    ),
    path(
        "articles/create/",
        ArticleCreateAPIView.as_view(),
        name="article-create",
    ),
]
