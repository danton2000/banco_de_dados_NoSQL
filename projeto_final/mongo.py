from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")

db = client["steam_games_db"]

jogos_collection = db["jogos"]