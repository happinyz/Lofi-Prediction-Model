import requests

# Sample requests file

URL = 'http://127.0.0.1:5000/predict'
headers = {"Content-Type": "application/json"}
data = {'input': [0.49, 0.715, -5.549, 1.0, 0.0476, 0.386, 0.0, 0.311, 0.866, 130.726]}

r = requests.get(URL, headers = headers, json=data)

r.json()