# codeing:utf-8
from django.urls import path
from .views import *


urlpatterns = [
    path(r'login/', login_view),
    path(r'logout/', logout_view),
    path(r'getUser/', get_user_view),
]
