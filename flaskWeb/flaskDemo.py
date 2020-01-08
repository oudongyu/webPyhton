# -*- coding:utf-8 -*-

"""
@Author : Oudongyu

@Time : 2020/1/8 14:33
"""

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_word():
    return 'hello word!'