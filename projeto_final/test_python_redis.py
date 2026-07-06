import redis

r = redis.Redis(
    host="localhost",
    port=6379,
    decode_responses=True
)

r.set("teste", "Olá Redis!")

print(r.get("teste"))