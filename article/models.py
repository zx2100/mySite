from django.db import models
from user.models import UserProfile
import django.utils.timezone as timezone
# Create your models here.


# 文章分类
class ArticleCategory(models.Model):
    name = models.CharField(max_length=40, unique=True, verbose_name="文章分类")

    class Meta:
        verbose_name = "文章分类"
        verbose_name_plural = verbose_name
        db_table = 'article_category'

    def __str__(self):
        return self.name


#  文章对象
class ArticlePost(models.Model):
    # 文章作者
    author = models.ForeignKey(UserProfile, on_delete=models.PROTECT, verbose_name="文章作者")
    ategory = models.ForeignKey(ArticleCategory, on_delete=models.CASCADE, verbose_name="文章分类")
    title = models.CharField(max_length=40, blank=False, default="未命名", verbose_name="标题")
    brief = models.CharField(max_length=100, blank=False, default="", verbose_name="文章简介")
    content = models.TextField(verbose_name="正文内容")
    create = models.DateTimeField(default=timezone.now, verbose_name="创建日期")
    update = models.DateTimeField(auto_now=True, verbose_name="更新日期")

    class Meta:
        verbose_name = "文章"
        verbose_name_plural = verbose_name
        db_table = 'article_post'

    def __str__(self):
        return self.title

