# importação de funções do módulo mongo_crud que serão utilizadas no menu
from mongo_crud import (
    inserir_jogo,
    listar_jogos,
    buscar_por_appid,
    buscar_por_nome,
    atualizar_jogo,
    deletar_jogo
)

# Importação de funções do módulo redis_service que serão utilizadas no menu
from redis_service import (
    gerar_rankings,
    listar_jogos_mais_positivos,
    listar_jogos_mais_negativos,
    listar_jogos_mais_caros,
    listar_jogos_mais_baratos,
    listar_jogos_mais_online
)

def mostrar_jogo(jogo):
    """Mostra os dados principais de um jogo."""
    if not jogo:
        print("Jogo não encontrado.")
        return

    print("-" * 50)
    print("AppID:", jogo.get("appid"))
    print("Nome:", jogo.get("name"))
    print("Desenvolvedora:", jogo.get("developer"))
    print("Publicadora:", jogo.get("publisher"))
    print("Preço:", jogo.get("price"))
    print("Avaliações positivas:", jogo.get("positive"))
    print("Avaliações negativas:", jogo.get("negative"))


def listar():
    """Lista alguns jogos cadastrados."""
    limite = int(input("Quantos jogos deseja listar? "))

    jogos = listar_jogos(limite)

    for jogo in jogos:
        mostrar_jogo(jogo)


def buscar_appid():
    """Busca um jogo pelo AppID."""
    appid = int(input("Digite o AppID do jogo: "))

    jogo = buscar_por_appid(appid)

    mostrar_jogo(jogo)


def buscar_nome():
    """Busca jogos pelo nome."""
    nome = input("Digite o nome ou parte do nome do jogo: ")

    jogos = buscar_por_nome(nome)

    if not jogos:
        print("Nenhum jogo encontrado.")
        return

    for jogo in jogos:
        mostrar_jogo(jogo)


def adicionar():
    """Adiciona um novo jogo manualmente."""
    print("\nCadastro de novo jogo")

    appid = int(input("AppID: "))
    name = input("Nome: ")
    developer = input("Desenvolvedora: ")
    publisher = input("Publicadora: ")
    price = input("Preço: ")
    positive = int(input("Avaliações positivas: "))
    negative = int(input("Avaliações negativas: "))

    jogo = {
        "appid": appid,
        "name": name,
        "developer": developer,
        "publisher": publisher,
        "price": price,
        "positive": positive,
        "negative": negative
    }

    id_inserido = inserir_jogo(jogo)

    print("Jogo inserido com sucesso!")
    print("ID gerado:", id_inserido)


def atualizar():
    """Atualiza informações básicas de um jogo."""
    appid = int(input("Digite o AppID do jogo que deseja atualizar: "))

    jogo = buscar_por_appid(appid)

    if not jogo:
        print("Jogo não encontrado.")
        return

    print("\nJogo encontrado:")
    mostrar_jogo(jogo)

    print("\nDigite os novos dados.")
    print("Deixe em branco para manter o valor atual.")

    novo_nome = input("Novo nome: ")
    novo_developer = input("Nova desenvolvedora: ")
    novo_publisher = input("Nova publicadora: ")
    novo_preco = input("Novo preço: ")

    dados_atualizados = {}

    if novo_nome:
        dados_atualizados["name"] = novo_nome

    if novo_developer:
        dados_atualizados["developer"] = novo_developer

    if novo_publisher:
        dados_atualizados["publisher"] = novo_publisher

    if novo_preco:
        dados_atualizados["price"] = novo_preco

    if not dados_atualizados:
        print("Nenhum dado foi alterado.")
        return

    alterados = atualizar_jogo(appid, dados_atualizados)

    if alterados > 0:
        print("Jogo atualizado com sucesso!")
    else:
        print("Nenhuma alteração realizada.")


def deletar():
    """Remove um jogo pelo AppID."""
    appid = int(input("Digite o AppID do jogo que deseja remover: "))

    jogo = buscar_por_appid(appid)

    if not jogo:
        print("Jogo não encontrado.")
        return

    print("\nJogo encontrado:")
    mostrar_jogo(jogo)

    confirmar = input("Tem certeza que deseja deletar? (s/n): ")

    if confirmar.lower() != "s":
        print("Operação cancelada.")
        return

    deletados = deletar_jogo(appid)

    if deletados > 0:
        print("Jogo deletado com sucesso!")
    else:
        print("Nenhum jogo foi deletado.")

def formatar_preco(valor):
    valor = abs(float(valor))
    return f"US$ {valor / 100:.2f}"

def mostrar_ranking(titulo, ranking, tipo=None):
    print("\n" + titulo)
    print("-" * 50)

    if not ranking:
        print("Ranking vazio. Gere os rankings primeiro.")
        return

    for posicao, item in enumerate(ranking, start=1):
        jogo, pontuacao = item

        if tipo == "preco":
            pontuacao = formatar_preco(pontuacao)

        print(f"{posicao}. {jogo} - {pontuacao}")

def gerar_rankings_redis():
    gerar_rankings()

def ranking_positivos():
    mostrar_ranking(
        "Jogos com mais avaliações positivas",
        listar_jogos_mais_positivos(10)
    )

def ranking_negativos():
    mostrar_ranking(
        "Jogos com mais avaliações negativas",
        listar_jogos_mais_negativos(10)
    )

def ranking_caros():
    mostrar_ranking(
        "Jogos mais caros",
        listar_jogos_mais_caros(10),
        tipo="preco"
    )

def ranking_baratos():
    mostrar_ranking(
        "Jogos mais baratos",
        listar_jogos_mais_baratos(10),
        tipo="preco"
    )

def ranking_online():
    mostrar_ranking(
        "Jogos com mais jogadores online",
        listar_jogos_mais_online(10)
    )

def menu():
    """Menu principal da aplicação."""
    while True:
        print("\n===== STEAM GAMES - NOSQL =====")

        print("\n--- MongoDB CRUD ---")
        print("1 - Listar jogos")
        print("2 - Buscar jogo por AppID")
        print("3 - Buscar jogo por nome")
        print("4 - Adicionar novo jogo")
        print("5 - Atualizar jogo")
        print("6 - Deletar jogo")

        print("\n--- Redis Rankings ---")
        print("7 - Gerar rankings no Redis")
        print("8 - Ranking jogos mais positivos")
        print("9 - Ranking jogos mais negativos")
        print("10 - Ranking jogos mais caros")
        print("11 - Ranking jogos mais baratos")
        print("12 - Ranking jogos com mais jogadores online")

        print("\n0 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            listar()
        elif opcao == "2":
            buscar_appid()
        elif opcao == "3":
            buscar_nome()
        elif opcao == "4":
            adicionar()
        elif opcao == "5":
            atualizar()
        elif opcao == "6":
            deletar()
        elif opcao == "7":
            gerar_rankings_redis()
        elif opcao == "8":
            ranking_positivos()
        elif opcao == "9":
            ranking_negativos()
        elif opcao == "10":
            ranking_caros()
        elif opcao == "11":
            ranking_baratos()
        elif opcao == "12":
            ranking_online()
        elif opcao == "0":
            print("Encerrando aplicação...")
            break
        else:
            print("Opção inválida.")


if __name__ == "__main__":
    menu()