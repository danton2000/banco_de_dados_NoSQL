from pymongo import MongoClient

try:
    client = MongoClient("mongodb://localhost:27017/")

    # Testa a conexão
    client.admin.command("ping")

    print("✅ Conexão realizada com sucesso!")

except Exception as e:
    print("❌ Erro:")
    print(e)