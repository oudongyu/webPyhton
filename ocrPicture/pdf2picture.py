# -*- coding: utf-8 -*-

from wand.image import Image
import os

# 将pdf文件转为jpg图片文件
cur_file_path = os.path.dirname(os.path.realpath(__file__))
# print cur_file_path
# path为pdf文件路径
# path = os.path.join(cur_file_path, os.pardir, 'ehouse/resource/img/')
path="D:\\tec\\华为\\"
image_pdf = Image(filename=path + r'华为大数据HCIA-大数据1.0-题库-下.pdf', resolution=300)
image_jpeg = image_pdf.convert('jpg')

# 页面转为独立的二进制图像对象
req_image = []
for img in image_jpeg.sequence:
    img_page = Image(image=img)
    req_image.append(img_page.make_blob('jpg'))

# 存储为图片文件
i = 0
for img in req_image:
    ff = open("D:\\tec\\HCIA-pictures\\" + str(i) + '.png', 'wb')
    ff.write(img)
    ff.close()
    i += 1