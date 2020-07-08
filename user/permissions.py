from rest_framework import permissions
import json
import base64
from .models import UserProfile


class OnlySuperAdmin(permissions.DjangoObjectPermissions):
    """
    自定义权限只允许对象的所有者编辑它。
    """
    message = "您的权限不允许此操作"

    def has_permission(self, request, view):
        # 获取用户名
        token_info = json.loads(base64.b64decode(request.headers["Authorization"].split(" ")[1].split(".")[1] + "=="))
        username = token_info['username']
        # 根据是否超级管理员返回结果
        return UserProfile.objects.filter(username=username).first().is_superuser


