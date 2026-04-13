from fastapi import FastAPI
import redis
import json

from config import REDIS_HOST, REDIS_PORT, REDIS_DB, QUEUE_NAME
from worker import start_worker_in_thread

redis_db = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, db=REDIS_DB)
app = FastAPI(title="Worker service")


@app.on_event("startup")
async def startup_event():
    start_worker_in_thread()


@app.get("/health")
async def health():
    return {"status": "ok"}


@app.post("/task")
async def enqueue_task(task: dict):
    redis_db.rpush(QUEUE_NAME, json.dumps(task))
    return {"status": "queued"}


@app.get("/task")
async def enqueue_task(task: dict):
    redis_db.get(QUEUE_NAME, json.dumps(task))
    return {"status": "ok"}

