#-*- coding:utf-8 -*-

"""
@Author : Oudongyu

@Time : 2020/1/8 15:54
"""

from django.http import HttpResponse

from HelloW.TestModel.models import Test


# 数据库操作
def testdb(request):
    test1 = Test(name='houda')
    test1.save()
    return HttpResponse("<p>数据添加成功！</p>")
