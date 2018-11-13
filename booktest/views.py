from django.shortcuts import render
from django.http import * #request,response

from  .models import *
# 要想使用模板 需要导入以下的包
from django.template import RequestContext,loader

# 定义视图Create your views here.
'''
视图view:
接受请求 逻辑处理 调用数据 输出相应
要有视图 就要有一个唯一的正则与它响应--->配置url(在自己的应用中配置正则)
'''


def index(request):
    '''
    # 去加载自己设置的模板 想要找到还需要去setting里面指定一个路径
    temp = loader.get_template('booktest/index.html')
    # temp.render() 去呈现自己模板内容,返回的结果就作为下面的内容
    return HttpResponse(temp.render())
'''
    bookList = BookInfo.objects.all()

    context = {'list':bookList}
    # 上面那样写太麻烦,这句话相当于封装了上面的动作
    # 第三个参数就是要用的数据
    return render(request,'booktest/index.html',context)

def show(request,id):
    book = BookInfo.objects.get(pk=id)
    # heroinfo_set表示这本书对应的所有英雄,是个列表/集合
    herolist = book.heroinfo_set.all()
    context = {'list':herolist}
    return render(request,'booktest/show.html',context)