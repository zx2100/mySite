from django.shortcuts import render
from rest_framework.response import Response
from django.http.response import HttpResponse
from rest_framework import status
# Create your views here.
from .models import *
from .serializers import ArticleGetSerializers, ArticlePostSerializers
from rest_framework.views import APIView


class MyResponse(Response):
    # 返回渲染器
    def __init__(self, code, msg, data, *arks, **kwargs):
        self.ret_msg = {
            "meta": {
                "status": code,
                "msg": msg
            },
            "data": data
        }
        super().__init__(self.ret_msg, *arks, **kwargs)


class GetALLView(APIView):
    permission_classes = []

    #获取文章
    def get(self, request):
        query_set = ArticlePost.objects.all()
        result = ArticleGetSerializers(query_set, many=True)
        # print(result)
        result = MyResponse(data=result.data, code=status.HTTP_200_OK, msg="获取成功")
        return result

    # 保存文章


class PostArticle(APIView):
    permission_classes = []

    def post(self, request):
        # print(request.data)

        # 验证数据
        serializer = ArticlePostSerializers(data=request.data)
        if serializer.is_valid():
            print("验证通过")
            serializer.save()
            print(serializer.data)
        else:
            print(serializer.errors)

        return Response(serializer.errors)
