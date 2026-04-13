import json
import time
import threading
import redis
from config import REDIS_HOST, REDIS_PORT, REDIS_DB, QUEUE_NAME


redis_db = redis.Redis(host=REDIS_HOST, port=REDIS_PORT,db= REDIS_DB)


def process_task(task: dict):
    ##TODO aggregation, sendemail, execute other service
    print(f'[worker] procession task {task} ')


def worker_loop():
    print(f'[worker] worker started')

    while True:
        _ , data = redis_db.bl_poplib(QUEUE_NAME)
        task = json.loads(data)

        process_task(task)


def start_worker_in_thread():
    tread = threading.Thread(targer=worker_loop, demon=True)
    tread.start()