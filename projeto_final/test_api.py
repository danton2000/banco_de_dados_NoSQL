import requests
import json
import urllib3

urllib3.disable_warnings()

url = "https://raw.githubusercontent.com/openfootball/worldcup.json/master/2026/worldcup.json"

response = requests.get(url, verify=False)

print("Status:", response.status_code)

if response.status_code == 200:
    dados = response.json()

    print("Chaves principais:", dados.keys())

    partidas = dados.get("matches", [])

    print("Total de partidas:", len(partidas))

    print("\nPrimeira partida:")
    print(json.dumps(partidas[0], indent=2, ensure_ascii=False))
else:
    print("Erro ao buscar dados:")
    print(response.text)