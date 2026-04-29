import random
import json

# 1. Criar um programa que possua listas pré-definidas com dados, como (nomes
# de produtos, preços, categorias, usuarios).

lista_nome_produtos = [
    "Logitech G Pro X Superlight Wireless Mouse",
    "Razer DeathAdder V3 Pro Mouse",
    "Corsair K95 RGB Platinum Mechanical Keyboard",
    "HyperX Alloy Origins Core Mechanical Keyboard",
    "Samsung Odyssey G7 27-inch Gaming Monitor",
    "LG UltraGear 34GP83A-B Ultrawide Monitor",
    "NZXT H510 Mid Tower Case",
    "Corsair iCUE 4000X RGB Case",
    "Kingston Fury Beast 16GB DDR4 RAM",
    "Corsair Vengeance RGB Pro 32GB DDR4 RAM"
]

lista_precos = [50, 100, 200, 300, 500, 800, 1000, 30, 80, 75]

lista_categorias = [
    "Perifericos",
    "Tecnologia",
    "Alimentacao",
    "Limpeza",
    "Pet",
    "Escritorio",
    "Moveis",
    "Roupas",
    "Saude",
    "Esportes"
]

lista_usuarios = [
    "Adalberto",
    "Alan Patrick",
    "Baldasso",
    "Ferraz",
    "Bruna",
    "Carlos Eduardo",
    "Daniela",
    "Fernanda",
    "Gustavo",
    "Mariana"
]

# 2. Gere automaticamente 1.000.000 de produtos aleatórios, combinando
# esses dados com (id, nome, preco, categoria, estoque e avaliações).

lista_produtos = []

for i in range(1, 1000001):

    indice_aleatorio = random.randrange(10)

    estoque_aleatorio = random.randrange(200)

    avaliacao_aleatorio = random.randrange(6)

    produto = {
        "nome": lista_nome_produtos[indice_aleatorio],
        "preco": lista_precos[indice_aleatorio],
        "categoria":lista_categorias[indice_aleatorio],
        "estoque": estoque_aleatorio,
        "avaliacao": [],
    }

    lista_produtos.append(produto)

#print(lista_produtos)
# 3. Gerar avaliações e colocar dentro do produtos aplicando Embedding.

for produto in lista_produtos:

    for i in range(random.randint(1, 5)):
        avaliacao = {
            "usuario": random.choice(lista_usuarios),
            "nota": random.randrange(6),
            "comentario": "Lorem ipsum dolor sit amet, consectetur adipiscing elit."
        }
        produto["avaliacao"].append(avaliacao)

#print(lista_produtos)

# 4. Salve o resultado em um arquivo .json
with open('dados.json', 'w', encoding='utf-8') as f:
    json.dump(lista_produtos, f, ensure_ascii=False, indent=4)