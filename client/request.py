import requests
import json

# Replace this URL with the ngrok URL printed by your Flask application
ngrok_url = 'https://5819-95-70-146-221.ngrok-free.app:5000/webhook'

# Example data to send, modify as needed
data_to_send = {
    'key': 'value',
    'example': 'data'
}

# Sending a POST request to your Flask webhook
response = requests.post(ngrok_url, json=data_to_send)

# Printing out the response from the server
print("Server responded with:", response.status_code, response.json())
