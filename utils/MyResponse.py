from rest_framework.response import Response


class MyResponse(Response):
    # 返回渲染器
    def __init__(self, code=204, msg="", data="", *arks, **kwargs):
        self.ret_msg = {
            "meta": {
                "status": code,
                "msg": msg
            },
            "data": data
        }
        super().__init__(self.ret_msg, *arks, **kwargs)
