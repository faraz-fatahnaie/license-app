import os

import requests

# Define the API endpoint
url = 'http://localhost:8000/api/activate_license'  # Replace with your actual endpoint URL

# Define the JSON payload
payload = {
    "activation_code": "45b2fcd2-efbd-4cb7-842f-aabc2b3c9e62",
    "hardware_unique_id": 'testCPU-testHardDrive'
}

api_key = os.getenv('API_KEY')
headers = {'API_KEY': api_key,
           'Content-Type': 'application/json'}

response = requests.post(url, json=payload, headers=headers)

# Check the response
if response.status_code == 200:
    print("Request was successful!")
    print("Response JSON:", response.json())
else:
    print("Request failed with status code:", response.status_code)
    print("Response JSON:", response.json())