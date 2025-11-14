from typing import Dict

import redis


class RedisUtility:
    def __init__(self, host: str, port: str, db: int, **kwargs: Dict):
        self.r = redis.Redis(host=host, port=port, db=db, **kwargs)

    def get(self, key):
        return self.r.get(name=key)

    def set(self, key, value, ttl):
        self.r.set(name=key, value=value, ex=ttl)

    def delete(self): ...

    def close(self):
        self.r.close()
