#-*- coding:utf-8 -*-

"""
@Author : Oudongyu

@Time : 2020/1/8 14:55
"""

from django.shortcuts import render


def hello(request):
    context = {}
    context['hello'] = 'Hello World!'
    return render(request, 'hello.html', context)