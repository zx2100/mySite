from rest_framework import permissions


class UserViewPremissions(permissions.DjangoObjectPermissions):
    """
    自定义权限只允许对象的所有者编辑它。
    """
    def has_permission(self, request, view):
        print(request.data)
        print(view.queryset)
        return True
