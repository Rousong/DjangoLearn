from django.db import models

'''
模型Model 负责与数据库交互
完全面向对象:操作模型对象  列表

定义模型类:指定属性及类型,以确定表的结构.迁移

后台管理:创建管理员,启动服务器, admin, 注册admin.py
         
'''

class BookInfo(models.Model):
    btitle = models.CharField(max_length=20)
    bpub_date = models.DateField()
    def __str__(self):
        return self.btitle

class HeroInfo(models.Model):
    hname = models.CharField(max_length=10)
    hgender = models.BooleanField()
    hcontent = models.CharField(max_length=1000)
    hbook = models.ForeignKey(BookInfo)

    def __str__(self):
        return self.hname


'''
shell 裡面的一些方法:

'''