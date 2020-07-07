# codeing:utf-8
from django.urls import path, re_path
from .views import *
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    path('auth', auth_view.as_view()),
    path('profile', UserProfileView.as_view()),
    path('profile/<int:pk>', UserProfileDetilView.as_view())
]
urlpatterns = format_suffix_patterns(urlpatterns)
