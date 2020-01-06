# -*- coding: utf-8 -*-
from docx import Document
from docx.shared import Inches

# document = Document("D:\\tec\\华为\\题库\\中级\\HCIP_test(ALL无答案版).docx")
# for paragraph in document.paragraphs:
#     print paragraph.text
f1 = open(r'D:\tec\HCIA-pictures\HCIP_test02.txt','w')
with open(r"D:\tec\HCIA-pictures\HCIP_test.txt", "r") as filename:
    lines = filename.readlines()
    for line in lines:
        # if line.lower().__contains__("answer") and len(line.strip()) > 0:
        if len(line.strip()) > 0:
            print (line.strip())
            f1.write(line.strip()+"\n")
f1.close()
