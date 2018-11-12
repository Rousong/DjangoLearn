# 一般来说一个应用要自己建立一个单独的url文件 这个是自己新建的
from django.conf.urls import url
from . import views
'''
   ^是正则表达式匹配字符串开始位置
   $是正则表达式匹配字符串结束位置
   '''
urlpatterns =[
    # 正则表达式 什么开头 什么结尾
    url(r'^$',views.index),
]
