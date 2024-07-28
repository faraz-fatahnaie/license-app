import requests

# Define the API endpoint
url = 'http://localhost:8000/api/activate_license'  # Replace with your actual endpoint URL

# Define the JSON payload
payload = {
    "activation_code": "eb7ed143-0be6-4276-bde3-eb9243fc936f",
    "hardware_unique_id": 'testCPU-testHardDrive'
}

# Send the POST request
response = requests.post(url, json=payload)

# Check the response
if response.status_code == 200:
    print("Request was successful!")
    print("Response JSON:", response.json())
else:
    print("Request failed with status code:", response.status_code)
    print("Response JSON:", response.json())