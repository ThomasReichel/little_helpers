import os
import csv
import time
import qrcode
import re
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

def create_qrCode(output_string):
    qr = qrcode.QRCode\
            (
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_L,
                box_size=5,
                border=0,
             )
    qr.add_data(output_string)
    qr.make(fit=True)
    qr_img = qr.make_image(fill_color="black", back_color="white")

    return qr_img


def get_year():
    year = time.strftime('%y')
    return year


def get_month():
    month = time.strftime('%m')
    return month


