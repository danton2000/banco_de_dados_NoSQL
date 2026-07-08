from redis_db import r
from mongo import jogos_collection


# Limpa os rankings antigos do Redis
def limpar_rankings():
    r.delete("ranking:jogos_positivos")
    r.delete("ranking:jogos_negativos")
    r.delete("ranking:jogos_caros")
    r.delete("ranking:jogos_baratos")
    r.delete("ranking:jogos_online")


# Gera os rankings com base nos dados do MongoDB
def gerar_rankings():
    limpar_rankings()

    jogos = jogos_collection.find()

    for jogo in jogos:
        nome = jogo.get("name")
        appid = jogo.get("appid")

        if not nome or not appid:
            continue

        chave_jogo = f"{appid} - {nome}"

        positivos = int(jogo.get("positive", 0) or 0)
        negativos = int(jogo.get("negative", 0) or 0)
        preco = int(jogo.get("price", 0) or 0)
        jogadores_online = int(jogo.get("ccu", 0) or 0)

        r.zadd("ranking:jogos_positivos", {chave_jogo: positivos})
        r.zadd("ranking:jogos_negativos", {chave_jogo: negativos})
        r.zadd("ranking:jogos_caros", {chave_jogo: preco})
        r.zadd("ranking:jogos_baratos", {chave_jogo: -preco})
        r.zadd("ranking:jogos_online", {chave_jogo: jogadores_online})

    print("Rankings gerados com sucesso no Redis!")


# Lista um ranking do maior para o menor
def listar_ranking(nome_ranking, limite=10):
    return r.zrevrange(
        nome_ranking,
        0,
        limite - 1,
        withscores=True
    )


def listar_jogos_mais_positivos(limite=10):
    return listar_ranking("ranking:jogos_positivos", limite)


def listar_jogos_mais_negativos(limite=10):
    return listar_ranking("ranking:jogos_negativos", limite)


def listar_jogos_mais_caros(limite=10):
    return listar_ranking("ranking:jogos_caros", limite)


def listar_jogos_mais_baratos(limite=10):
    return listar_ranking("ranking:jogos_baratos", limite)


def listar_jogos_mais_online(limite=10):
    return listar_ranking("ranking:jogos_online", limite)