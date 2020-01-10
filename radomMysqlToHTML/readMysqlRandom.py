# -*- coding:utf-8 -*-

"""
@Author : Oudongyu

@Time : 2020/1/6 22:38
"""
import pymysql
import random
import os


def randomTest(pathfile):
    if not os.path.isfile(pathfile):
        t = open(pathfile, mode="w", encoding="utf-8")
        t.close()
    f1 = open(pathfile, "w", encoding="utf-8")
    html01 = '''<!doctype html>
    <html lang="en">
    <head>
    <meta charset="UTF-8">
    <style>
    .div_bor{
    border:1px solid #274b8b ;
    padding: 5px 10px 10px 5px;
    }
    </style>
    </head>
    <body>
    <div class="div_bor">
    '''
    f1.write(html01 + "\n")
    testRandom = []
    testAnswer = []
    # 此循环作用： 抽题100道，不同重复的题
    while (testRandom.__len__() < 3):
        x = random.randint(1, fetchone.__len__())
        if x not in testRandom:
            testRandom.append(x)
    # print(testRandom)
    for num, t in enumerate(testRandom, start=1):
        # print("<p>{}</p>".format(num.__str__() + " " + fetchone[t - 1][1]))
        f1.write("<p>{}</p>\n".format(num.__str__() + fetchone[t - 1][1].strip()))
        split = fetchone[t - 1][-3].split("\n")
        # print(fetchone[t - 1][-2])
        testAnswer.append(fetchone[t - 1][-2])
        if fetchone[t - 1][-1] == "dan":
            for i in split:
                # print("<p><input type=\"radio\" name=\"A\">{}</p>".format(i))
                f1.write("<p><input type=\"radio\" name=\"{}\">{}</p>\n".format(num, i))
        else:
            for i in split:
                # print("<p><input type=\"checkbox\">{}</p>".format(i))
                f1.write("<p><input type=\"checkbox\">{}</p>\n".format(i))
    # print("""</div>
    # </body>
    # </html>
    #     """)
    f1.write("<p><button style=\"float: right\" onclick=\"fn()\">确定</button></p></div>\n<script>\n")
    f1.write("var rule = {};\n".format(testAnswer.__str__()))
    f1.write("""var boxs = document.getElementsByTagName('input');
alert(boxs)
var check = [];
var score = 0;
function fn(){
check=[];
score = 0;
for(var i=0;i<boxs.length;i++){
if(boxs[i].checked){
check.push(boxs[i].value);
}
}
for(var j=0;j<check.length;j++){
if(rule.indexOf(check[j]) !=-1){
score++;
}else{
score--;
}
}
alert(Math.ceil(100/rule.length*score)+'分');
}
</script>""")
    f1.close()


if __name__ == '__main__':
    db = pymysql.connect("localhost", 'root', 'root', 'phpt')
    cursor = db.cursor()
    sql = "select * from hciabigdata"
    cursor.execute(sql)
    fetchone = cursor.fetchall()
    randomTest("./test.html")
