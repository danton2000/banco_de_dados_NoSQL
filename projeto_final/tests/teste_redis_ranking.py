from redis_service import (
    gerar_rankings,
    listar_jogos_mais_positivos,
    listar_jogos_mais_caros,
    listar_jogos_mais_online,
    listar_jogos_mais_negativos,
    listar_jogos_mais_baratos
)

def formatar_preco(valor):
    valor = abs(float(valor))
    return f"U$ {valor / 100:.2f}".replace(".", ",")

def mostrar_ranking(titulo, ranking, tipo=None):
    print("\n" + titulo)
    print("-" * 50)

    for posicao, item in enumerate(ranking, start=1):
        jogo, pontuacao = item

        if tipo == "preco":
            pontuacao = formatar_preco(pontuacao)

        print(f"{posicao}. {jogo} - {pontuacao}")


gerar_rankings()

mostrar_ranking(
    "Jogos com mais avaliações positivas",
    listar_jogos_mais_positivos(10)
)

mostrar_ranking(
    "Jogos mais caros",
    listar_jogos_mais_caros(10),
    tipo="preco"
)

mostrar_ranking(
    "Jogos com mais jogadores online",
    listar_jogos_mais_online(10)
)

mostrar_ranking(
    "Jogos com mais avaliações negativas",
    listar_jogos_mais_negativos(10)
)

mostrar_ranking(
    "Jogos mais baratos",   
    listar_jogos_mais_baratos(10),
    tipo="preco"
)