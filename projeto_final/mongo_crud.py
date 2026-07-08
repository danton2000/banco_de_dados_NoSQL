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