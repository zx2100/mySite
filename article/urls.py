# codeing:utf-8
from django.urls import path, re_path
from .views import *
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    path('all', GetALLView.as_view()),
    path('post', PostArticle.as_view()),
]
