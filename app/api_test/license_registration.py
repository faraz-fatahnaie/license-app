import hashlib
import os

import requests

# Define the API endpoint
url = 'http://localhost:8000/api/create_license'  # Replace with your actual endpoint URL

# Define the JSON payload
payload = {
    "tarabari_id": "test_transport_id",
    "additional_days": 10
}

api_key = os.getenv('REG_API_KEY')

headers = {'REG_API_KEY': api_key,
           'Content-Type': 'application/json'}
response = requests.post(url, json=payload, headers=headers)

# Check the response
if response.status_code == 200:
    print("Request was successful!")
    print("Response JSON:", response.json())
else:
    print("Request failed with status code:", response.status_code)
    print("Response JSON:", response.json())