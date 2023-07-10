import redis
from loguru import logger


class RedisCache:
    def __init__(self, host, port=6379, password=None):
        self._host = host
        self._port = port
        self._password = password
        self._pool = None
        self._r = None
        logger.debug('RedisCache initialization complete')

    def create_pool(self):
        pool = redis.ConnectionPool(host=self._host, port=self._port, password=self._password)
        self._pool = pool

    def get_redis(self):
        try:
            r = redis.Redis(connection_pool=self._pool, decode_responses=True, charset='UTF-8', encoding='UTF-8')
            self._r = r
            logger.info(self._pool)
            # 成功获取连接对象，表示连接池创建成功
            logger.debug('Connection to redis success')
            return r
        except redis.exceptions.ConnectionError as e:
            logger.error(e)

    def check_key(self, key):
        if self._r.get(key):
            return True
        else:
            return False

    def get(self, key):
        return self._r.get(key)

    def set(self, key, value):
        if not self.check_key(key):
            reply = self._r.set(key, value, ex=300)
            return reply
        logger.debug('Cache succeeded')
