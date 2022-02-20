from django.urls import path
from .views import ArticleViewSet

article_list = ArticleViewSet.as_view({
    'get': 'list',
    'post': 'create',
})


urlpatterns = [
    path('', article_list)
]
