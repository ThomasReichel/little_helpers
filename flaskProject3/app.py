from flask import Flask, request, render_template, url_for, redirect
from flask_bootstrap import Bootstrap
import pandas as pd   # from pandas import read_csv

import lib
import lib_mini
import lib_pw

app = Flask(__name__)
Bootstrap(app)


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/login')
def login():
    return render_template("index.html")

@app.route('/leeres_Label')
def leeres_label():
    return render_template("leeres_Label.html")

@app.route('/FTP_Label')
def ftp_label():
    return render_template("FTP_Label.html")

@app.route('/PW_Label')
def pw_label():
    return render_template("PW_Label.html")

@app.route('/MC_Label')
def mc_label():
    return render_template("MC_Label.html")

@app.route('/MC_altes_Label')
def mc_altes_label():
    return render_template("MC_altes_Label.html")

@app.route('/X300_flashen')
def x300_flashen():
    return render_template("X300_flashen.html")

@app.route('/X300_Label')
def x300_label():
    return render_template("X300_Label.html")

@app.route('/X300_altes_Label')
def x300_altes_label():
    return render_template("X300_altes_Label.html")

@app.route('/L5000_flashen')
def l5000_flashen():
    return render_template("L5000_flashen.html")

@app.route('/L5000_Label')
def l5000_label():
    return render_template("L5000_Label.html")

@app.route('/L5000_altes_Label')
def l5000_altes_label():
    return render_template("L5000_altes_Label.html")

@app.route('/NG_v2_flashen')
def ng_v2_flashen():
    return render_template("NG_v2_flashen.html")

@app.route('/NG_v2_Label')
def ng_v2_label():
    return render_template("NG_v2_Label.html")

@app.route('/NG_v2_altes_Label')
def ng_v2_altes_label():
    return render_template("NG_v2_altes_Label.html")

@app.route('/NG_v3_flashen')
def ng_v3_flashen():
    return render_template("NG_v3_flashen.html")

@app.route('/NG_v3_Label')
def ng_v3_label():
    return render_template("NG_v3_Label.html")

@app.route('/NG_v3_altes_Label')
def ng_v3_altes_label():
    return render_template("NG_v3_altes_Label.html")


if __name__ == '__main__':
    app.run(debug=True)

