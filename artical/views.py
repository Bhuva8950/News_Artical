
from rest_framework import generics, status
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Article
from .serializers import (
    ArticleCreateSerializer,
    ArticleSerializer,
)
# from .helper import extract_article

class ArticleCreateAPIView(APIView):
    def post(self, request):
        serializer = ArticleCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        # url = serializer.validated_data["url"]
        # requested_status = serializer.validated_data.get(
        #     "status",
        #     Article.Status.PENDING,
        # )
        # data = extract_article(url)
        # serializer.save(**data, status=requested_status)


        return Response(
            {"message":"Artical Created Successfully",
            "data":serializer.data
            },
            status=status.HTTP_201_CREATED,
        )


class ArticleListAPIView(generics.ListAPIView):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()

    def get_queryset(self):
        queryset = super().get_queryset()
        # Add filters for status and company name
        article_status = self.request.query_params.get("status")
        company_name = self.request.query_params.get("company_name")

        if article_status:
            queryset = queryset.filter(status=article_status)

        if company_name:
            queryset = queryset.filter(
                company_name__icontains=company_name
            )

        return queryset
