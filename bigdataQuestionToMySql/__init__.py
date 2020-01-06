# -*- coding: utf-8 -*-

import pymysql
import json

if __name__ == '__main__':
    db=pymysql.connect("localhost",'root','root','phpt')

    cursor=db.cursor()
    sql="desc stu"
    cursor.execute(sql)
    fetchone = cursor.fetchone()
    print(fetchone)
    # a={'name':'hd','age':'27'}
    # load = json.loads(a)
    # print(load['name'])
    d01 = {}
    for m, n in enumerate(range(10)):
        d01[m]=n
    print(d01)
