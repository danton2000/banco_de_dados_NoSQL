import requests
import json
import urllib3

urllib3.disable_warnings()

url = "https://steamspy.com/api.php"

params = {
    "request": "appdetails",
    "appid": 730
}

response = requests.get(url, params=params, verify=False)

print("Status:", response.status_code)

if response.status_code == 200:
    dados = response.json()
    print(json.dumps(dados, indent=4, ensure_ascii=False))
else:
    print(response.text)