from flask import Flask, request, render_template
from flask_bootstrap import Bootstrap
import pandas as pd   # from pandas import read_csv

import lib
import lib_mini
import lib_pw

app = Flask(__name__)
Bootstrap(app)

df = pd.read_csv("test.csv")
print(df)



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/pw_label')
def pw_label():
    return render_template('pw_label.html')

@app.route('/pw_print', methods=['POST', 'GET'])
def new_pw():
    pw = request.form['pw']
    anzahl = request.form['anzahl']
    output = lib.get_outputstring(pw)
    lib_pw.create_img(output)
    lib_pw.print_label(anzahl)
    return render_template('pw_print.html', pw=pw, anzahl=anzahl)


@app.route('/minicluster')
def minicluster():
    return render_template('minicluster.html')


@app.route('/minicluster_newLabel')
def minicluster_newLabel():
    return render_template('minicluster_newLabel.html')


@app.route('/minicluster_mac')
def minicluster_mac(datensatz):
    input_mac = request.form['mini_mac']
    anzahl = request.form['anzahl']
    lib_mini.get_deviceMAC(datensatz, input_mac)
    lib_mini.set_newDaten_MC(datensatz)
    output = lib_mini.get_outputString_MC(datensatz)
    lib_mini.create_label_MC(output)
    lib_mini.print_label(anzahl)


@app.route('/minicluster_printNewLabel')
def minicluster_printNewLabel():
    anzahl = request.form['anzahl']
    device = request.form['device']
    spezifi = request.form['spezifi']
    lft_Nr = request.form['lft_Nr']
    output = lib_mini.get_outputString_MC_newLabel(anzahl, device, spezifi, lft_Nr)
    lib_mini.create_label_MC(output)
    lib_mini.print_label(anzahl)

if __name__ == '__main__':
    app.run(debug=True)

