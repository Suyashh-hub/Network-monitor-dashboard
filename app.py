from flask import Flask, render_template
import json
from datetime import datetime
from monitor import (
    ping_host,
    get_server_stats
)

app = Flask(__name__)


@app.route("/")
def dashboard():

    with open("devices.json") as f:
        devices = json.load(f)

    results = []

    for device in devices:

        status = ping_host(device["ip"])

        device_data = {
            "name": device["name"],
            "ip": device["ip"],
            "status": status
        }

        if (
            status == "UP"
            and "username" in device
            and "password" in device
        ):

            stats = get_server_stats(
                device["ip"],
                device["username"],
                device["password"]
            )

            device_data.update(stats)

        results.append(device_data)

    current_time = datetime.now().strftime("%I:%M:%S %p")

    return render_template(
        "dashboard.html",
        devices=results,
        current_time=current_time
    )

if __name__ == "__main__":
    app.run(debug=True)
