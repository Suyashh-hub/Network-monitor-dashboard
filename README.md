# Network Monitoring Dashboard

A Python + Flask based Network and Server Monitoring Dashboard built using Linux (WSL), Flask, Paramiko, and GitHub.

## Features

* Device status monitoring using ping
* SSH-based Linux server monitoring
* CPU usage monitoring
* RAM usage monitoring
* Disk usage monitoring
* Flask web dashboard
* JSON-based device configuration
* Real-time monitoring architecture

## Technologies Used

* Python
* Flask
* Paramiko
* Linux / Ubuntu WSL
* Git & GitHub
* HTML
* JSON

## Project Structure

network-monitor/
│
├── app.py
├── monitor.py
├── devices.json
├── requirements.txt
├── templates/
│ └── dashboard.html
├── venv/
└── README.md

## How to Run

### Clone Repository

```bash
git clone https://github.com/Suyashh-hub/Network-monitor-dashboard.git
cd Network-monitor-dashboard
```

### Create Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Application

```bash
python3 app.py
```

Open browser:

```text
http://127.0.0.1:5000
```

## Current Features Completed

* Phase 1: Basic Flask Dashboard
* Phase 2: SSH-Based Linux Monitoring

## Upcoming Features

* Auto refresh dashboard
* Beautiful UI
* Graphs and charts
* Email alerts
* Real-time monitoring
* Cloud deployment

## Author

Suyash Nandeshwar

