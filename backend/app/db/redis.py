import redis
from app.config.settings import settings

client = redis.Redis(
    host=settings.REDIS_HOST,
    port=6379,
    decode_responses=True
)

def check_redis():
    try:
        client.ping()
        return True
    except Exception as e:
        print(f"Redis Error: {e}")
        return False