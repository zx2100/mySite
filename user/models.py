from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class UserProfile(AbstractUser):
    """
    用户信息,继承django默认的user模型，新增几个字段
    django提供的字段（重要的，次要的不写了,源码有）
    username
    email
    is_staff : 是否能登录admin站点
    is_active: 是否激活
    date_joined
    is_superuser :是否超级用户
    """
    # 用户名称，显示名称
    name = models.CharField(max_length=20, null=True, blank=True, verbose_name="姓名")
    birthday = models.DateField(null=True, blank=True, verbose_name="出生年月")
    # 性别，通过choices限制只有2个选项，字符串形式存储
    gender = models.CharField(max_length=6, choices=(("male", u"男"), ("female", u"女")), default="male", verbose_name="性别")
    phone_number = models.CharField(max_length=20, blank=True, verbose_name="电话号码")
    is_vip = models.BooleanField(default=False, verbose_name="是否会员")

    class Meta:
        db_table = 'user_profile'
        verbose_name = "用户"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username

    # 设置密码
