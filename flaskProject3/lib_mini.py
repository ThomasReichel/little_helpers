import os
import csv
import time
import qrcode
import re
import lib
from PIL import Image, ImageFont, ImageDraw

def get_deviceMAC(datensatz, input_mac):
    match = re.match('([a-fA-F0-9]{2}[:]?){6}', input_mac)
    if (match):
        datensatz['MAC'] = input_mac


def get_lftNr_MC():
        path = "Minicluster_SNr.csv"
        with open(path, 'rt') as file:
            header = ['device', 'spezifi', 'MAC', 'Jahr', 'Monat', 'lft_Nr']
            csvReader = csv.DictReader(file, header)
            content = [row for row in csvReader]
            last = content[-1]
            lastLft = int(last['lft_Nr'])
            aktLftNr = lastLft + 1

        return aktLftNr


def get_outputString_MC(datensatz):
    stringForSerienNr = "www.lucom.de\n{0}.{1}.18.{2}\n192.168.1.200\n".format(datensatz['device'], datensatz['spezifi'], datensatz['lft_Nr'])
    return stringForSerienNr


def get_outputString_MC_newLabel(anzahl, device, spezifi, lft_Nr):
    stringForNewLabel = "www.lucom.de\n{0}.{1}.18.{2}\n192.168.1.200\n".device, spezifi, lft_Nr
    return stringForNewLabel



def set_newDaten_MC(datensatz):
    try:
        path = "Minicluster_SNr.csv"
        with open(path, 'a') as fileOutput:
            header = ['device', 'spezifi', 'MAC', 'Jahr', 'Monat', 'lft_Nr']
            csvWriter = csv.DictWriter(fileOutput, header)
            csvWriter.writerow(datensatz)
    except:
        print("Die Daten konnten nicht in die CSV-Datei geschrieben werden!")

    return 0




# Dictionary befüllen
def fill_Dict_MC(datensatz):
    datensatz['device'] = 'MC'
    datensatz['spezifi'] = '03'
    datensatz['Jahr'] = lib.get_year()
    datensatz['Monat'] = lib.get_month()
    tmp_number = str(get_lftNr_MC())
    datensatz['lft_Nr'] = tmp_number.zfill(3)
    return datensatz


# QR-Code erstellen
def create_label_MC(output):
    global img
    try:
        qr_img = create_qrCode(output)
        create_img(qr_img, output)

    except Exception as e:
        print("Der QR-Code konnte nicht erstellt werden!")
        raise (e)

    return 0

def create_qrCode(output):
    qr = qrcode.QRCode\
            (
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_L,
                box_size=5,
                border=0,
             )
    qr.add_data(output)
    qr.make(fit=True)
    qr_img = qr.make_image(fill_color="black", back_color="white")

    return qr_img


def create_img(qr_img, output):
    # Label erstellen
    img = Image.new('1', (614, 283), color='white')
    d = ImageDraw.Draw(img)
    fonts = lib.get_fonts()
    fontPath = 'NotoSansMono-Regular.ttf'
    if (fontPath not in fonts):
        fontPath = [i for i in fonts if ("mono" in i.lower())][0]
    font = ImageFont.truetype(fontPath, 40)
    d.text((70, 5), output, font=font, fill='black')

    # QR Code in png einfügen
    width, height = qr_img.size
    img.paste(qr_img, (605 - width, 17))
    # png speichern
    img.save('mc_snr.bmp')
    return 0


def print_label(anzahl):
    try:
        for i in range(int(anzahl)):
            os.system('lp mc_snr.bmp')
            time.sleep(1)
            while (os.popen("lpstat").read()):
                time.sleep(0.2)
        print("Programm erfolgreich beendet")

    except:
        print("Drucker nicht angeschlossen!")

    return 0
