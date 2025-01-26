import requests

url = "http://127.0.0.1:5000/api/parks/search"
headers = {"Content-Type": "application/json"}
data = {
    "SwingSet": True,
    "WaterPlay": True
}

response = requests.post(url, json=data, headers=headers)
print(response.status_code)
print(response.json())
