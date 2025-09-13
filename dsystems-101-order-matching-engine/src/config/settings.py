# settings.py

KAFKA_BROKER_URL = 'localhost:9092'
KAFKA_TOPIC = 'order-matching'
REDIS_HOST = 'localhost'
REDIS_PORT = 6379
REDIS_DB = 0

LOG_LEVEL = 'INFO'
ORDER_TIMEOUT = 30  # seconds
MAX_RETRIES = 5

# Add any additional configuration settings as needed.