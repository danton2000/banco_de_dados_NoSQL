from mongo_crud import (
    inserir_jogo,
    listar_jogos,
    buscar_por_appid,
    buscar_por_nome,
    buscar_por_desenvolvedora,
    listar_jogos_gratis,
    atualizar_jogo,
    deletar_jogo,
    listar_jogos_mais_caros,
    listar_jogos_mais_positivos
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


def buscar_desenvolvedora():
    """Busca jogos por desenvolvedora."""
    developer = input("Digite o nome da desenvolvedora: ")

    jogos = buscar_por_desenvolvedora(developer)

    if not jogos:
        print("Nenhum jogo encontrado.")
        return

    for jogo in jogos:
        mostrar_jogo(jogo)


def listar_gratis():
    """Lista jogos gratuitos."""
    jogos = listar_jogos_gratis(10)

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

def listar_mais_caros():
    jogos = listar_jogos_mais_caros()

    for jogo in jogos:
        mostrar_jogo(jogo)

def listar_mais_positivos():
    jogos = listar_jogos_mais_positivos()

    for jogo in jogos:
        mostrar_jogo(jogo)


def menu():
    """Menu principal da aplicação."""
    while True:
        print("\n===== STEAM GAMES - MONGODB CRUD =====")
        print("1 - Listar jogos")
        print("2 - Buscar jogo por AppID")
        print("3 - Buscar jogo por nome")
        print("4 - Buscar jogos por desenvolvedora")
        print("5 - Listar jogos grátis")
        print("6 - Adicionar novo jogo")
        print("7 - Atualizar jogo")
        print("8 - Deletar jogo")
        print("9 - Listar jogos mais caros")
        print("10 - Listar jogos com mais avaliações positivas")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            listar()
        elif opcao == "2":
            buscar_appid()
        elif opcao == "3":
            buscar_nome()
        elif opcao == "4":
            buscar_desenvolvedora()
        elif opcao == "5":
            listar_gratis()
        elif opcao == "6":
            adicionar()
        elif opcao == "7":
            atualizar()
        elif opcao == "8":
            deletar()
        elif opcao == "9":
            listar_mais_caros()
        elif opcao == "10":
            listar_mais_positivos()
        elif opcao == "0":
            print("Encerrando aplicação...")
            break
        else:
            print("Opção inválida.")


if __name__ == "__main__":
    menu()