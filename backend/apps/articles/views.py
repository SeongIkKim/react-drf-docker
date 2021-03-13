from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet
from .models import Article
from .serializers import ArticleSerializer


class ArticleViewSet(ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [AllowAny]
