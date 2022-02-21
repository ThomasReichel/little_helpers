from  flask import Flask

registry = {}

app = Flask(__name__)

@app.route("/")
def index():
    # if instance existiert nicht -> erzeugen
    if registry["lobix"] == None:
        device = Device(name, alter)
        registry["lobix"] = device
        device_inst = registry["lobix"]
    else:
        # ansonsten nur ausgeben
        device_inst = registry["lobix"]

    device_inst.get_name()

