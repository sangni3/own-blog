# def img_add_text(filename,textcont):
#     #1、打开图片
#     image = Image.open(filename).convert('RGB') # 图片是400x300 宽x高
#     #print(image.size)
#     width=image.size[0]
#     height=image.size[1]
#     #2、定义字体和大小
#     fnt=ImageFont.truetype("c:/Windows/fonts/msyhl.ttc",
# size=int(width/20))
#     #3、新建图层
#     draw = ImageDraw.Draw(image)
#     #4、在当前图层上写文字
#     draw.text(xy=(width-
# (int(width/20)*len(textcont)),int(height*9/10)),text=textcont,font=fnt
# ,fill=(255,255,255,255))
#     #5、显示
#     return image
#
# from PIL import Image,ImageDraw,ImageFont
# image=img_add_text("../Demo/web/static/timg.bmp",'好好学习,天天向上')
# image.show(),
# image.save("../Demo/web/static/timg2.bmp")
import math
from random import random


def assgin_name(len):
    b = len
    a = random()
    a = int(a * math.pow(10, b))
    a = str(a) + 'jpg'
    return a



