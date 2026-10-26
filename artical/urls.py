
from django.urls import path

from .views import (
    ArticleCreateAPIView,
    ArticleListAPIView,
    ProcessArtical
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
    path(
        "articles/process/",
        ProcessArtical.as_view(),
        name="article-process",
    ),
]
