# Python DevOps Monitoring Tool

A server monitoring script that checks CPU, memory, disk, status, ping, and HTTP for a list of servers.

## Setup

1. Clone the repo
2. Create a virtual environment:
   python3 -m venv .venv
   source .venv/bin/activate
3. Install dependencies:
   pip install -r requirements.txt
4. Copy .env.example to .env and fill in values

## Usage

Run the monitoring script:
   python scripts/monitor_v4.py

Run the log parser:
   python scripts/log_parser.py
