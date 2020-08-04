from django.db import models
from user.models import UserProfile
# Create your models here.
import mongoengine
from mongoengine import queryset_manager
import datetime
import time

# 文章分类
class ArticleCategory(models.Model):
    name = models.CharField(max_length=40, unique=True, verbose_name="文章分类")

    class Meta:
        verbose_name = "文章分类"
        verbose_name_plural = verbose_name
        db_table = 'article_category'

    def __str__(self):
        return self.name


#  文章对象/Mysql 取消使用
# class ArticlePost(models.Model):
#     # 文章作者
#     author = models.ForeignKey(UserProfile, on_delete=models.PROTECT, verbose_name="文章作者")
#     ategory = models.ForeignKey(ArticleCategory, on_delete=models.CASCADE, verbose_name="文章分类")
#     title = models.CharField(max_length=40, blank=False, default="未命名", verbose_name="标题")
#     brief = models.CharField(max_length=100, blank=False, default="", verbose_name="文章简介")
#     content = models.TextField(verbose_name="正文内容")
#     create = models.DateTimeField(default=timezone.now, verbose_name="创建日期")
#     update = models.DateTimeField(auto_now=True, verbose_name="更新日期")
#
#     class Meta:
#         verbose_name = "文章"
#         verbose_name_plural = verbose_name
#         db_table = 'article_post'
#
#     def __str__(self):
#         return self.title


class MyQuerySet(mongoengine.QuerySet):
    # 获取一些数据
    def get_some(self, count):
        data = []
        # 字段排除
        except_field = ["id"]
        # 获取数据，可以在self中指定获取多少条数据
        for item in self[:count]:
            obj = {}
            for field in item:
                # 排除字段
                if field in except_field:
                    continue
                #  序列化时间
                if field == "created" or field == "updated":
                    item[field] = str(item[field]).split('.')[0] if item[field] else ""

                obj[field] = str(item[field])
            data.append(obj)
        return data


class Articles(mongoengine.Document):
    author = mongoengine.StringField(required=True, max_length=100)  # 作者,应该判断是否为当前用户
    category = mongoengine.StringField(required=True, max_length=100)  # 文章分类
    title = mongoengine.StringField(required=True, max_length=100)  # 标题
    brief = mongoengine.StringField(required=True, max_length=100)  # 内容简介
    content = mongoengine.StringField(required=True)  # Markdown的文章内容
    created = mongoengine.DateTimeField(required=True)  # 创建时间
    updated = mongoengine.DateTimeField()  # 修改时间
    meta = {
        'collection': 'articles',  # 存放到指定集合中
        'db_alias': 'mongodb',  # 选择连接的数据库实例
        'queryset_class': MyQuerySet  # 自定义过滤器
    }


