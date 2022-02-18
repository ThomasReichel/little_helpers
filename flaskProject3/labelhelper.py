import re
import csv
import lib
import os
import time
import pandas as pd
from PIL import Image, ImageFont, ImageDraw

class Labelhelper:

    def __init__(self, device_name, specification):
        self.data_set = {}
        self.device = device_name
        self.spezification = specification
        self.img_path = 'img/' + self.device + '.bmp'
        self.csv_path = 'csv/' + self.device + '.csv'

    def get_deviceMAC(self, input_mac):
        match = re.match('([a-fA-F0-9]{2}[:]?){6}', input_mac)
        if match:
            self.data_set['MAC'] = input_mac
            return self.data_set

    def get_lftNr(self):
       # with open(self.csv_path, 'rt') as file:
        #    header = ['device', 'spezifi', 'MAC', 'Jahr', 'Monat', 'lft_Nr']
        #    csvReader = csv.DictReader(file, header)
        #   content = [row for row in csvReader]
        #    last = content[-1]
        #    lastLft = int(last['lft_Nr'])
        #    aktLftNr = lastLft + 1
        df = pd.read_csv(self.csv_path)
        lastLft = df.iloc[(len(df) - 1)][5]
        aktLftNr = lastLft + 1

        return aktLftNr

    def fill_Dict(self, device_name, spezification):
        self.data_set['device'] = device_name
        self.data_set['spezifi'] = spezification
        self.data_set['Jahr'] = lib.get_year()
        self.data_set['Monat'] = lib.get_month()
        tmp_number = str(lib.get_lftNr())
        self.data_set['lft_Nr'] = tmp_number.zfill(3)
        return self.data_set

    def set_newDaten(self):
        try:
            path = self.data_set['device'] + ".csv"
            with open(path, 'a') as fileOutput:
                header = ['device', 'spezifi', 'MAC', 'Jahr', 'Monat', 'lft_Nr']
                csvWriter = csv.DictWriter(fileOutput, header)
                csvWriter.writerow(self.data_set['device'], self.data_set['device'], self.data_set['device'],
                                   self.data_set['device'], self.data_set['device'], self.data_set['lft_Nr'])
        except:
            print("Die Daten konnten nicht in die CSV-Datei geschrieben werden!")

        return 0

    def get_outputString(self):
        output_string = "www.lucom.de\n{0}.{1}.18.{2}\n192.168.1.200\n".format(self.data_set['device'],
                                                        self.data_set['spezifi'], self.data_set['lft_Nr'])
        return output_string

    def create_label(self, output):
        global img
        try:
            qr_img = lib.create_qrCode(output)
            lib.create_img(qr_img, output)

        except Exception as e:
            print("Der QR-Code konnte nicht erstellt werden!")
            raise (e)
        return 0

    def create_img(self, qr_img, output_string):
        # Label erstellen
        img = Image.new('1', (614, 283), color='white')
        d = ImageDraw.Draw(img)
        fonts = lib.get_fonts()
        fontPath = 'NotoSansMono-Regular.ttf'
        if (fontPath not in fonts):
            fontPath = [i for i in fonts if ("mono" in i.lower())][0]
        font = ImageFont.truetype(fontPath, 40)
        d.text((70, 5), output_string, font=font, fill='black')

        # QR Code in png einfügen
        width, height = qr_img.size
        img.paste(qr_img, (605 - width, 17))
        # png speichern
        img.save(self.img_path)
        return 0

    def print_label(self, anzahl=3):
        try:
            for i in range(int(anzahl)):
                os.system('lp' + self.img)
                time.sleep(1)
                while (os.popen("lpstat").read()):
                    time.sleep(0.2)
            print("Programm erfolgreich beendet")

        except:
            print("Drucker nicht angeschlossen!")

        return 0
