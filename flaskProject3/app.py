import lib
from flask_bootstrap import Bootstrap
from flask import Flask, request, render_template, url_for


app = Flask(__name__)
Bootstrap(app)


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
    output = lib.get_outputString(pw)
    lib.create_img(output)
    lib.print_label(anzahl)
    return render_template('pw_print.html', pw=pw, anzahl=anzahl)

if __name__ == '__main__':
    app.run(debug=True)

