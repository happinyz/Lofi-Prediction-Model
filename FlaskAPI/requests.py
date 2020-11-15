import requests

# Sample requests file

URL = 'http://127.0.0.1:5000/predict'
headers = {"Content-Type": "application/json"}
data = {'input': [0.807,0.576,-10.158,0,0.296,0.0419,0.931,0.116,0.771,169.999]}

r = requests.get(URL, headers = headers, json=data)

r.json()
