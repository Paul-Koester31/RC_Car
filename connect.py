from flask import Flask, render_template, request
import bluetooth

app = Flask(__name__)

# Bluetooth-Geräte in der Nähe scannen
def scan_devices():
    nearby_devices = bluetooth.discover_devices(duration=8, lookup_names=True)
    devices = [(addr, name) for addr, name in nearby_devices]
    return devices

@app.route('/')
def index():
    devices = scan_devices()
    return render_template('controller.html', devices=devices)

@app.route('/connect', methods=['POST'])
def connect():
    selected_device = request.form['device']
    # Hier fügst du den Code hinzu, um dich mit dem ausgewählten Gerät zu verbinden
    return f"Connecting to device: {selected_device}"

if __name__ == '__main__':
    app.run(debug=True)
