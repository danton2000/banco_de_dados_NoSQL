import requests
import json
import urllib3

urllib3.disable_warnings()

url = "https://steamspy.com/api.php"

params = {
    "request": "all",
    "page": 1
}

response = requests.get(url, params=params, verify=False)

print("URL final:", response.url)
print("Status:", response.status_code)

if response.status_code == 200:
    dados = response.json()

    print("Quantidade de jogos:", len(dados))

    for appid, jogo in list(dados.items())[:10]:  # Exibe apenas os 10 primeiros jogos
        
        print(appid, "-", jogo.get("name"))
else:
    print(response.text)

print("Fim do teste da API.")