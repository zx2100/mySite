# # from .models import ArticlePost
# from rest_framework import serializers
# import time
#
#
# # 获取文章
# class ArticleGetSerializers(serializers.ModelSerializer):
#     # serializers.PrimaryKeyRelatedField(many=True, queryset=UserProfile.objects.all())
#     author = serializers.CharField(source='author.username', read_only=True)
#     category = serializers.CharField(source='category.name', read_only=True)
#
#     # 重写序列化方法，对需要的字段进行自定义渲染（时间字段的返回需要序列化）
#     def to_representation(self, instance):
#         result = super().to_representation(instance)
#         # 抽取时间，序列化时间
#         create = time.strptime(result['create'].split(".")[0], "%Y-%m-%dT%H:%M:%S")
#         update = time.strptime(result['update'].split(".")[0], "%Y-%m-%dT%H:%M:%S")
#         result['create'] = time.strftime('%Y-%m-%d %H:%M', create)
#         result['update'] = time.strftime('%Y-%m-%d %H:%M', update)
#         # 处理简介
#         result = self.to_brief(result)
#         # 组成文章简介。如
#
#         return result
#
#     def to_brief(self, obj):
#         """
#
#         :param obj:
#         :return: 处理简介内容
#         简介内容如果没有，则返回正文的前50-100个字符
#         """
#         if obj["brief"] == "":
#             obj["brief"] = obj["content"][:90] + "..."
#         #     如果简介本身大于73字符，则返前面73个字符
#         elif len(obj["brief"]) > 90:
#             obj["brief"] = obj["brief"][:90] + "..."
#         return obj
#
#     class Meta:
#         model = ArticlePost
#         fields = '__all__'
#         # 获取深度，如果有字段外键的话，就往里面再次获取
#         # depth = 1
#
#
# # 提交文章
# class ArticlePostSerializers(serializers.ModelSerializer):
#
#     # def create(self, validated_data):
#     #     print(validated_data)
#     #     return ArticlePost(**validated_data)
#
#     # 验证数据
#     def validate(self, data):
#         # 验证文章简介是否超出100字符
#         if len(data["brief"]) > 100:
#             raise serializers.ValidationError("文章简介内容过长，应该小于100字符")
#         return data
#
#     class Meta:
#         model = ArticlePost
#         fields = '__all__'
