
from rest_framework import serializers

from .models import Article,ArticalData


class ArticleCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ["url"]

    def validate_url(self, value):
        if Article.objects.filter(url=value).exists():
            raise serializers.ValidationError(
                "This article URL already exists."
            )
        return value


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = [
            "id",
            "url",
            "status"
        ]
        read_only_fields = fields

class ArticleDataCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArticalData
        fields = ["title","article","content","category","summary","created_at"]

    # def validate_url(self, value):
    #     if Article.objects.filter(url=value).exists():
    #         raise serializers.ValidationError(
    #             "This article URL already exists."
    #         )
    #     return value