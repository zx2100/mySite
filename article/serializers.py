from .models import ArticlePost
from rest_framework import serializers


class ArticlePostSerializers(serializers.ModelSerializer):
    # serializers.PrimaryKeyRelatedField(many=True, queryset=UserProfile.objects.all())

    class Meta:
        model = ArticlePost
        fields = [
            'author', 'ategory', 'title', 'content', 'create', 'update'
        ]