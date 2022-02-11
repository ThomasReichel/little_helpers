import os
import re
import time
from PIL import Image, ImageFont, ImageDraw

def get_outputstring(password):
    string = "User:\n dcadmin\nPasswort:\n {}".format(password)
    return string

def get_fonts():
    fc_list = os.popen("fc-list").read().split("\n")
    ret = []
    for fc in fc_list:
        match = re.match(r".*/(.*\.ttf)", fc)
        if match:
            ret.append(match.groups(0)[0])
    return ret


def get_year():
    year = time.strftime('%y')
    return year


def get_month():
    month = time.strftime('%m')
    return month


