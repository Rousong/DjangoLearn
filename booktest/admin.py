from django.contrib import admin
from .models import *
# python3 不加点的话，就找不到
# 注册模型类 Register your models here.

# inline 内部嵌套
class HeroInfoInline(admin.StackedInline):
    '''
    继承StackedInline就是多个表单
    如果继承TabularInline的话就是表格形式
    '''
    # 选择你要选择哪个模型类 嵌套进去
    model = HeroInfo
    # 额外添加几个数据
    extra = 3


#定义一个类 可以对后台显示的界面显示的字段进行编辑
class BookInfoAdmin(admin.ModelAdmin):
    #定义显示的字段 可以点击列头进行排序
    list_display = ['id','btitle','bpub_date']
    #定义一个过滤器 过滤框会显示在右侧
    list_filter = ['btitle']
    # 查找
    search_fields = ['btitle']
    # 显示多少页 分页框会显示在下侧
    list_per_page = 1

    # [修改页和修改页]可以设置修改数据页面的分类
    fieldsets = [
        ('一个分类',{'fields':['btitle']}),
        ('另一个分类',{'fields':['bpub_date']})
    ]

    # 定义要嵌入的 列表内可以写多个
    inlines = [HeroInfoInline]

# 注册模型 (模型类,admin类[定义在这句话之前,要继承admin.ModelAdmin])
admin.site.register(BookInfo,BookInfoAdmin)
admin.site.register(HeroInfo)