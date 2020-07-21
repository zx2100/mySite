from .models import ArticlePost
from rest_framework import serializers
import time


class ArticlePostSerializers(serializers.ModelSerializer):
    # serializers.PrimaryKeyRelatedField(many=True, queryset=UserProfile.objects.all())
    # author = serializers.CharField(source='author.username', read_only=True)
    # category = serializers.CharField(source='category.name', read_only=True)

    # 重写序列化方法，对需要的字段进行自定义渲染（时间字段的返回需要序列化）
    def to_representation(self, instance):
        result = super().to_representation(instance)
        # 抽取时间，序列化时间
        create = time.strptime(result['create'], "%Y-%m-%dT%H:%M:%S")
        update = time.strptime(result['update'].split(".")[0], "%Y-%m-%dT%H:%M:%S")
        result['create'] = time.strftime('%Y-%m-%d %H:%M', create)
        result['update'] = time.strftime('%Y-%m-%d %H:%M', update)
        return result

    def create(self, validated_data):
        """
        给定验证过的数据创建并返回一个新的 Snippet 实例。
        """
        return ArticlePost.objects.create(**validated_data)

    class Meta:
        model = ArticlePost
        fields = '__all__'
        # 获取深度，如果有字段外键的话，就往里面再次获取
        depth = 1
