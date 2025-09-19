import requests

# URL of your Flask app
url = 'http://127.0.0.1:5000/customer'  # Adjust if running on a different host/port

# Data to send
data = {
    'name': 'Vikas',
    'age': 23,
    'balance': 450000.75
}

# Send POST request
response = requests.post(url, json=data)

# Print response
print('Status Code:', response.status_code)
print('Response:', response.json())
