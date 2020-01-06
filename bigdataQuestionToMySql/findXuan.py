# -*- coding: utf-8 -*-
import os
import re
import bigdataQuestionToMySql.finalVar
# 读取文本，将所有题的完整题干写入到新的文件
import pymysql


def step01(sourcePath, srcPath):
    listIndex = []
    listLine = []
    listQuestion = []
    # 将每行的内容写入listline，将开头为数字的写入listindex
    with open(sourcePath, "r", encoding="utf-8") as f4:
        for m, n in enumerate(f4):
            listLine.append(n.strip())
            if re.match("^[\\d+]", n):
                listIndex.append(m)
    # print(listIndex,listLine)
    listSelect = {}
    inSelect(listSelect, listQuestion, listIndex, listLine)

    # print(listSelect.get(122))

    #     将listQuestion中 在多行的问题，拼接到一行。
    # print(listQuestion)
    #
    # f1 = open(srcPath, "w", encoding="utf-8")
    # for i in listQuestion:
    #     if re.match('[\\d+]', i):
    #         print(i)
    #         f1.write("\n" + i)
    #     else:
    #         f1.write(i)
    # f1.close()


# "问题编号，问题 ， 选项"  放到dict中
def inSelect(listSelect, listQuestion, listIndex, listLine):
    # print(listLine)
    # print(listIndex)
    for num, i in enumerate(listIndex, start=1):
        selectQuestion = []
        listQuestion.append(listLine[i])
        if num != listIndex.__len__():
            for j in listLine[i + 1:]:
                if not re.match('^[\\d+]', j):
                    if re.match('^[abcdftABCDTF]| ', j):
                        selectQuestion.append(j)
                    else:
                        listQuestion.append(listQuestion[-1] + j)
                        listQuestion.pop(-2)
                else:
                    listSelect[num] = "\n".join(selectQuestion)
                    break
        else:
            for j in listLine[i + 1:]:
                if re.match('^[abcdftABCDTF]| ', j):
                    selectQuestion.append(j)
                listSelect[num] = "\n".join(selectQuestion)
    answer = getAnswer(listQuestion, listSelect)
    # print(answer)
    writeToMysql(answer)


def step02(sourcePath, srcPath):
    listIndex = []  # 包含组件题目的下标
    with open(sourcePath, "r", encoding="utf-8") as f4:
        listLine = [line for line in f4]
    f3 = open(srcPath, "r", encoding="utf-8")
    # 这个for循环作用：找出包含相关题目的所有下标
    for i in f3:
        # 查找hdfs相关题目
        # if i.lower().__contains__("hdfs") or \
        #         i.lower().__contains__("namenode") or \
        #         i.lower().__contains__("datanode") or \
        #         i.lower().__contains__("dn"):
        # if i.lower().__contains__("mapreduce") or \
        #         i.lower().__contains__("yarn") or \
        #         i.lower().__contains__("contain") or \
        #         i.lower().__contains__("资源"):
        # if i.lower().__contains__("spark") or i.lower().__contains__("executor") or i.lower().__contains__("task"):
        # if i.lower().__contains__("hbase") or \
        #         i.lower().__contains__("region") or i.lower().__contains__("hflie") or \
        #         i.lower().__contains__("master"):
        # if i.lower().__contains__("hive"):
        if i.lower().__contains__("zookeeper"):
            # i.lower().__contains__("leader") or \
            # i.lower().__contains__("flower")
            for m in listLine:
                if m == i:
                    listIndex.append(listLine.index(m))
    # print (listIndex)
    # print(listLine.__len__())
    # print(listLine[110])
    for i in listIndex:
        print(listLine[i].strip())
        for j in listLine[i + 1:]:
            if re.match("^[\\d+]", j):
                break
            print(j.strip())


def step03(sourcePath, srcPath):
    listIndex = []
    with open(sourcePath, "r", encoding="utf-8") as f4:
        listLine = [line for line in f4]
    with open(srcPath, "r", encoding="utf-8") as f5:
        for i in f5:
            for m in listLine:
                if m == i:
                    listIndex.append(listLine.index(m))
    for m, i in enumerate(listIndex):
        print(listLine[i].strip())
        for j in listLine[i + 1:]:
            if re.match("^[\\d+]", j):
                break
            print(j.strip())


#  获取每题的 题号，答案，多选or单选
def getAnswer(listQuestion, listSelect):
    listAll = []
    pattern = re.compile(r'[a-fA-F]+')
    patternNum = re.compile(r'[\d]+')
    for num, lineQuestion in enumerate(listQuestion, start=1):
        findall = pattern.findall(lineQuestion)
        num_findall = patternNum.findall(lineQuestion)
        answer = findall[-1]
        newLine = " ".join(lineQuestion.rsplit(findall[-1], 1))
        newLine = "".join(newLine.rsplit(num_findall[0], 1))
        if len(answer) > 1:
            listAll.append(newLine.strip() + bigdataQuestionToMySql.finalVar.FIELDSPLIT +
                           listSelect[num] + bigdataQuestionToMySql.finalVar.FIELDSPLIT +
                           findall[-1] + bigdataQuestionToMySql.finalVar.FIELDSPLIT + "duo")
        else:
            listAll.append(newLine.strip() + bigdataQuestionToMySql.finalVar.FIELDSPLIT +
                           listSelect[num] + bigdataQuestionToMySql.finalVar.FIELDSPLIT +
                           findall[-1] + bigdataQuestionToMySql.finalVar.FIELDSPLIT + "dan")
    return listAll


def writeToMysql(listAll):
    db = pymysql.connect("localhost", 'root', 'root', 'phpt')
    cursor = db.cursor()
    usersvalues = []  # 定义一个列表
    for m, n in enumerate(listAll):
        split = n.split(bigdataQuestionToMySql.finalVar.FIELDSPLIT)
        # print(split)
        usersvalues.append((split[0], split[1], split[2], split[3]))
    # print(usersvalues.__len__())
    sql = "insert into hciabigdata(question," \
          "options," \
          "answer," \
          "ifmulti) " \
          "values (%s,%s,%s,%s)"
    try:
        cursor.executemany(sql,usersvalues)
        db.commit()
    except:
        db.rollback()
    cursor.close()
    db.close()


if __name__ == '__main__':
    step01(r"D:\tec\HCIA-pictures\hciabigdata.txt",
           r"D:\tec\HCIA-pictures\TG2hciabigdata.txt")
# step02(r"D:\tec\HCIA-pictures\hciabigdata.txt",
#        r"D:\tec\HCIA-pictures\TGhciabigdata.txt")
# step03(r"D:\tec\HCIA-pictures\hciabigdata.txt",
#        r"D:\tec\HCIA-pictures\TGhciabigdata.txt")

# getAnswer(r"D:\tec\HCIA-pictures\TG2hciabigdata.txt")
# ss="12344"
# rsplit = ss.rsplit("4", 1)
# print(rsplit)

# writeToMysql()
