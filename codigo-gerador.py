import os
import random
import json
import csv

downloads = os.path.join(os.path.expanduser("~"), "Downloads")
json_path = os.path.join(downloads, "produtos.json")
csv_path = os.path.join(downloads, "produtos.csv")

nome_prod = ['pizza', 'shampoo', 'mouse', 'café', 'capinha celular']
preco = [30, 20, 50, 40, 10]
categoria = ['comida', 'higiene', 'eletronico', 'bebida', 'acessorio']
usuario = ['João', 'Maria', 'José', 'Pedro', 'Lucas', 'Ana', 'Breno']

catalogo = []

for i in range(1000000) : 
    produto = {
        "nome": random.choice(nome_prod),
        "preco" : random.choice(preco),
        "categoria" :  random.choice(categoria),
        "estoque": random.randint(1,10),
        "avaliações":[]
    }
    for i in range(random.randint(1,5)):
        avaliacao = {
            "usuario" : random.choice(usuario),
            "nota" : random.randint(1,5),
            "comentario": "Bom produto"
        }
        produto['avaliações'].append(avaliacao)
    catalogo.append(produto)

# ... gerar catalogo ...
with open(csv_path, "w", encoding="utf-8", newline="") as csvfile:
    fieldnames = ["nome", "preco", "categoria", "estoque", "avaliacoes"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for produto in catalogo:
        writer.writerow({
            "nome": produto["nome"],
            "preco": produto["preco"],
            "categoria": produto["categoria"],
            "estoque": produto["estoque"],
            "avaliacoes": json.dumps(produto["avaliações"], ensure_ascii=False)
        })