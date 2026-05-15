from flask import Flask, render_template
import json

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

    return render_template(
        "dashboard.html",
        devices=results
    )


if __name__ == "__main__":
    app.run(debug=True)
