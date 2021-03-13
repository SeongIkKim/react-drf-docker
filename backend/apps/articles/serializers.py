from rest_framework import serializers
from . import models


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Article
        fields = ("id", "title", "content", "created_at", "updated_at")
