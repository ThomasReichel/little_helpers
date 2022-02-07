# -*- coding: utf-8 -*-
import os
import re
import time
from PIL import Image, ImageFont, ImageDraw

def get_outputString(password):
    string = "User:\n dcadmin\nPasswort:\n {}".format(password)
    return string

def get_fonts():
    fc_list = os.popen("fc-list").read().split("\n")
    ret = []
    for fc in fc_list:
        match = re.match(r".*\/(.*\.ttf)", fc)
        if(match):
            ret.append(match.groups(0)[0])
    return ret



def create_img(output):
    img = Image.new('1', (614, 283), color='white')
    d = ImageDraw.Draw(img)
    fonts = get_fonts()
    fontPath = 'NotoSansMono-Regular.ttf'

    if (fontPath not in fonts):
        fontPath = [i for i in fonts if ("mono" in i.lower())][0]

    font = ImageFont.truetype(fontPath, 40)
    d.text((100, 5), output, font=font, fill='black')
    img.save('new_pw.bmp')
    return 0


def print_label(anzahl):
    try:
        for i in range(int(anzahl)):
            os.system('lp new_pw.bmp')
            time.sleep(1)
            while (os.popen("lpstat").read()):
                time.sleep(0.2)
        print("Programm erfolgreich beendet")

    except:
        print("Drucker nicht angeschlossen!")

    return 0