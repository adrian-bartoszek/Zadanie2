from flask import Flask, request
import datetime
import time
import requests
import os

app = Flask(__name__)
start_time = time.strftime("%Y-%m-%d %H:%M:%S")

# Get environment variable ports
container_port = os.environ.get('PORT', '5000')
host_port = os.environ.get('HOST_PORT', '5000')

def get_user_ip():
    response = requests.get('https://ipapi.co/ip/')
    return response.text.strip()

def get_user_timezone(ip_address):
    url = f'https://ipapi.co/{ip_address}/timezone/'
    response = requests.get(url)
    return response.text.strip()

# Get current date information
def get_current_date():
    return start_time.split()[0]

def get_current_time():
    return start_time.split()[1]

# Handle GET request
@app.route('/')
def hello():
    user_ip = get_user_ip()
    user_timezone = get_user_timezone(user_ip)
    current_date = get_current_date()
    current_time = get_current_time()
    more_info = log_server_start()
    user_ip = get_user_ip()
    user_timezone = get_user_timezone(user_ip)

    response = f"<h3>Client Information</h3>Client IP Address: {user_ip}<br>Client timezone: {user_timezone}<br><h3>Server Information</h3>Server Start Date: {current_date} {current_time}<br>Container Port: {container_port}<br>Host Port: {host_port}<br><h3>More Information</h3>{more_info}"
    return response


# Handle GET request for health check
@app.route('/health')
def health_check():
    return 'OK', 200

# Display author and date information
def log_server_start():
    author_name = "Adrian Bartoszek"
    now = datetime.datetime.now()
    start_time = now.strftime("%Y-%m-%d %H:%M:%S")
    log_info = f"Server started by: {author_name}<br>Current date and time: {start_time}"
    print(log_info)
    return log_info

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)