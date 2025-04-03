import redis
import json
from app.config import Config  # Adjust import if needed

# Connect to Redis
redis_client = redis.StrictRedis(
    host="redis", port=6379, db=0, decode_responses=True
)

def set_cache(key, value, expiry=3600):
    """Set data in Redis with an expiration time (default: 1 hour)."""
    redis_client.setex(key, expiry, json.dumps(value))

def get_cache(key):
    """Retrieve data from Redis."""
    data = redis_client.get(key)
    return json.loads(data) if data else None

def delete_cache(key):
    """Delete a cache entry from Redis."""
    redis_client.delete(key)
