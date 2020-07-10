from .models import ArticlePost
from rest_framework import serializers


class ArticlePostSerializers(serializers.ModelSerializer):
    # serializers.PrimaryKeyRelatedField(many=True, queryset=UserProfile.objects.all())
    author = serializers.CharField(source='author.username', read_only=True)
    ategory = serializers.CharField(source='ategory.name', read_only=True)

    class Meta:
        model = ArticlePost
        fields = '__all__'
