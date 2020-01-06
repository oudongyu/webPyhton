# -*- coding: utf-8 -*-
import os
from docx import Document
from aip import AipOcr

""" 你的 APPID AK SK """
APP_ID = '18034133'
API_KEY = 'QabrxTayeHriy6LXBhuUGVkc'
SECRET_KEY = 'eykCsKakGdK6SeuzfBCunqbCkovBDhxN'

client = AipOcr(APP_ID, API_KEY, SECRET_KEY)
document = Document()
# print(client)


def renameFile(path):
    listdir = os.listdir(path)
    for i in listdir:
        print(i.split(" ")[1])
        os.rename(path+"\\"+i,path+"\\"+i.split(" ")[1])


""" 读取图片 """

def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()


def get_path_allPicture(picturePath):
    list = []
    for path in os.listdir(picturePath):
        if path.endswith(".jpg") or path.endswith(".png"):
            list.append(picturePath+'\\'+path)
    print(list)
    return list


def get_pictire_words(path,path2):
    image = get_file_content(path)
    """ 调用通用文字识别, 图片参数为本地图片 """
    # client.basicGeneral(image)
    """ 如果有可选参数 """
    options = {}
    options["language_type"] = "CHN_ENG"
    options["detect_direction"] = "true"
    options["detect_language"] = "true"
    options["probability"] = "true"

    """ 带参数调用通用文字识别, 图片参数为本地图片 """
    datas = client.basicGeneral(image, options)

    for i in datas["words_result"]:
        print(i["words"])
        document.add_paragraph(i["words"])
    document.save(path2)


if __name__ == '__main__':
    # pictureList = get_path_allPicture(r"D:\tec\HCIA-pictures")
    # pictureList = get_path_allPicture(r"D:\tec\HCIA-pictures\hcia")
    pictureList = get_path_allPicture(r"D:\tec\HCIA-pictures\realText")
    for file in pictureList:
        get_pictire_words(file,u'D:\\tec\\HCIA-pictures\\HCIA-hua.docx')

    # renameFile(r"D:\tec\HCIA-pictures\hcia")