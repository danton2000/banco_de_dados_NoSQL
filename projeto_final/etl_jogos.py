import requests
import urllib3
from mongo import jogos_collection

urllib3.disable_warnings()

URL = "https://steamspy.com/api.php"


def extrair_jogos():
    params = {
        "request": "all",
        "page": 0
    }

    response = requests.get(URL, params=params, verify=False)

    print("Status da API:", response.status_code)

    if response.status_code != 200:
        print("Erro ao buscar dados da SteamSpy")
        print(response.text)
        return []

    dados = response.json()

    jogos = []

    for appid, jogo in dados.items():
        jogos.append({
            "appid": int(appid),
            "name": jogo.get("name"),
            "developer": jogo.get("developer"),
            "publisher": jogo.get("publisher"),
            "score_rank": jogo.get("score_rank"),
            "positive": int(jogo.get("positive", 0)),
            "negative": int(jogo.get("negative", 0)),
            "userscore": int(jogo.get("userscore", 0)),
            "owners": jogo.get("owners"),
            "average_forever": jogo.get("average_forever", 0),
            "average_2weeks": jogo.get("average_2weeks", 0),
            "median_forever": jogo.get("median_forever", 0),
            "median_2weeks": jogo.get("median_2weeks", 0),
            "price": int(jogo.get("price", 0)),
            "initialprice": jogo.get("initialprice"),
            "discount": jogo.get("discount"),
            "ccu": jogo.get("ccu", 0)
        })

    return jogos


def carregar_mongodb(jogos):
    if not jogos:
        print("Nenhum jogo para inserir.")
        return

    # Limpar a coleção antes de inserir novos dados
    jogos_collection.delete_many({})

    resultado = jogos_collection.insert_many(jogos)

    print(f"Jogos inseridos no MongoDB: {len(resultado.inserted_ids)}")


def listar_amostra():
    print("\nAmostra dos jogos no MongoDB:")

    for jogo in jogos_collection.find().limit(5):
        print({
            "appid": jogo.get("appid"),
            "name": jogo.get("name"),
            "developer": jogo.get("developer"),
            "positive": jogo.get("positive"),
            "negative": jogo.get("negative")
        })


if __name__ == "__main__":
    jogos = extrair_jogos()

    print(f"Jogos extraídos: {len(jogos)}")

    carregar_mongodb(jogos)

    listar_amostra()