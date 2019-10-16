from celery import Celery

# TODO: Put these in config possibly.
CELERY_BROKER_URL = 'redis://localhost:6379/0'
CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'

celery = Celery('ghost-task', broker=CELERY_BROKER_URL, backend=CELERY_RESULT_BACKEND)

celery.conf.update(BROKER_URL=CELERY_BROKER_URL, CELERY_RESULT_BACKEND=CELERY_RESULT_BACKEND)

@celery.task
def hello(msg):
    return "Hello. Here is your msg: " + msg