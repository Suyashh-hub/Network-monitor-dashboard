from flask import Flask, render_template
import json
from monitor import ping_host

app = Flask(__name__)

@app.route("/")
def dashboard():
    with open("devices.json") as f:
        devices = json.load(f)

    results = []

    for d in devices:
        status = ping_host(d["ip"])
        results.append({
            "name": d["name"],
            "ip": d["ip"],
            "status": status
        })

    return render_template("dashboard.html", devices=results)

if __name__ == "__main__":
    app.run(debug=True)
