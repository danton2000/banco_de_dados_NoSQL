from mongo import jogos_collection


# CREATE - inserir um novo jogo
def inserir_jogo(jogo):
    resultado = jogos_collection.insert_one(jogo)
    return resultado.inserted_id


# READ - listar jogos
def listar_jogos(limite=10):
    return list(jogos_collection.find().limit(limite))


# READ - buscar por AppID
def buscar_por_appid(appid):
    return jogos_collection.find_one({"appid": appid})


# READ - buscar por nome
def buscar_por_nome(nome):
    return list(jogos_collection.find({
        "name": {"$regex": nome, "$options": "i"}
    }).limit(10))


# READ - buscar por desenvolvedora
def buscar_por_desenvolvedora(developer):
    return list(jogos_collection.find({
        "developer": {"$regex": developer, "$options": "i"}
    }).limit(10))


# READ - listar jogos grátis
def listar_jogos_gratis(limite=10):
    return list(jogos_collection.find({
        "price": 0
    }).limit(limite))


# UPDATE - atualizar jogo pelo AppID
def atualizar_jogo(appid, novos_dados):
    resultado = jogos_collection.update_one(
        {"appid": appid},
        {"$set": novos_dados}
    )
    return resultado.modified_count


# DELETE - remover jogo pelo AppID
def deletar_jogo(appid):
    resultado = jogos_collection.delete_one({"appid": appid})
    return resultado.deleted_count

# READ - listar jogos mais caros
def listar_jogos_mais_caros(limite=10):
    return list(
        jogos_collection.find().sort("price", -1).limit(limite)
    )


# READ - listar jogos com mais avaliações positivas
def listar_jogos_mais_positivos(limite=10):
    return list(
        jogos_collection.find().sort("positive", -1).limit(limite)
    )