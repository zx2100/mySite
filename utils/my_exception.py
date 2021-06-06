from rest_framework.views import exception_handler
from utils.my_response import MyResponse
from rest_framework import status
from rest_framework.exceptions import APIException

def custom_exception_handler(exc, context):
    # 先调用REST framework默认的异常处理方法获得标准错误响应对象
    response = exception_handler(exc, context)
    # 在此处补充自定义的异常处理
    if response is not None:
        response.data['status_code'] = response.status_code

    return MyResponse(code=response.data.get('status_code'), msg=response.data.get("detail"))



class XdError(APIException):
    pass


class ParamError(XdError):
    status_code = 400


class Unauthorized(XdError):
    status_code = 401


class PermissionDenied(XdError):
    status_code = 403


class ObjectNotFound(XdError):
    status_code = 404


class ServerError(XdError):
    status_code = 500


class ErrorCode:
    UNAUTHORIZED = 10000  # 未登录
    PERMISSION_DENIED = 10001  # 无权限
    PARAM_ERROR = 40000  # 参数验证错误
    DATA_NOT_FOUND = 40001  # 未找到数据
    DATA_NOT_VALID = 40002  # 数据错误
    REPEAT_POST = 40003  # 重复提交
    EEEE = 40003  # 新型错误