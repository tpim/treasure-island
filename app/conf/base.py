"""配置"""

DEBUG = True
MONGODB_SETTINGS = {
    'host': 'mongodb://root:123456@localhost:27017/treasure_island?authSource=admin'
}

CELERY_RESULT_BACKEND = 'redis://localhost:6379'
CELERY_BROKER_URL = 'redis://localhost:6379'
