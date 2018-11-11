from django.contrib import admin
from .models import *
# python3 不加点的话，就找不到
# 注册模型类 Register your models here.


#定义一个类 可以对后台显示的界面显示的字段进行编辑
class BookInfoAdmin(admin.ModelAdmin):
    list_display = ['id','btitle','bpub_date']
    #定义一个过滤器
    list_filter = ['btitle']

admin.site.register(BookInfo,BookInfoAdmin)
admin.site.register(HeroInfo)