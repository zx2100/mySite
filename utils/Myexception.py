from rest_framework.views import exception_handler
from utils.MyResponse import MyResponse


def custom_exception_handler(exc, context):
    # 先调用REST framework默认的异常处理方法获得标准错误响应对象
    response = exception_handler(exc, context)
    # 在此处补充自定义的异常处理
    if response is not None:
        response.data['status_code'] = response.status_code

    return MyResponse(code=response.data.get('status_code'), msg=response.data.get("detail"))
