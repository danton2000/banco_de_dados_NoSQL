import redis

# Conexão com o Redis local
r = redis.Redis(
    host="localhost",
    port=6379,
    decode_responses=True
)