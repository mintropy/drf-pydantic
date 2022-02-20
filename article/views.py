import datetime
from typing import List

from django.shortcuts import get_list_or_404
from djantic import ModelSchema
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response

from .models import Article

# Create your views here.
class ArticleSchema(ModelSchema):
    created_at: datetime.datetime = datetime.datetime.now()

    class Config:
        model = Article


class ArticleViewSet(ViewSet):
    model = Article
    queryset = Article.objects.all()

    def list(self, request):
        articles = get_list_or_404(Article)
        articles_schema: List[ArticleSchema] = ArticleSchema.from_django(articles, many=True)
        return Response(
            [
                article_schema.dict()
            ]
            for article_schema in articles_schema
        )

    def create(self, request):
        article_data = ArticleSchema(**request.data)
        article = Article.objects.create(**article_data.dict())
        article = ArticleSchema.from_django(article)
        return Response(article.dict())
