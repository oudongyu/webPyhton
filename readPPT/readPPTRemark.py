# -*- coding: utf-8 -*-
import win32com
import re
from win32com.client import Dispatch, constants
import time

ppt = win32com.client.Dispatch('PowerPoint.Application')
ppt.Visible = 1
pptSel = ppt.Presentations.Open(
    r"D:\tec\华为\HCIP-Big Data Developer V2.0 培训材料\HCIP-Big Data Developer V2.0 培训教材&实验手册\第一章 大数据应用开发总指导.pptx")
win32com.client.gencache.EnsureDispatch('PowerPoint.Application')
f = open(r"D:\tec\in.txt", "w")
noteList = []
slide_count = pptSel.Slides.Count
for i in range(1, slide_count + 1):
    shape_count = pptSel.Slides(i).Shapes.Count
    note = pptSel.Slides(i).NotesPage.Shapes.Placeholders(2).TextFrame.TextRange.Text
    # noteList.append(note)
    # print(note)
    time.sleep(3)
    print(shape_count)
