# External Imports
import os
import redis
from rq import Worker, Queue, Connection

# Ankra Imports
from ankra import Config, get_logger
from ankra.utils.network import is_online

logging = get_logger(name="worker")

config = Config(fetch_app_secret=False,
                fetch_app_config=False)
configs = config.load_dict_config()

# Redis Config.
worker_name = os.getenv('MY_POD_NAME', 'worker-01')
listen = ['default']
conn = redis.from_url(f"{configs['REDIS_URL']}/4")

if __name__ == '__main__':
    # Check if Redis is online.
    if is_online(configs['REDIS_URL'].split('redis://')[1]):
        with Connection(conn):
            logging.info(f"Registering worker with name: {worker_name}")
            # Check if a worker with the same name exists.
            workers = Worker.all(connection=conn)
            if workers:
                for worker in workers:
                    logging.info(f"Found active worker: {worker.name}")
                    if worker_name in worker.name:
                        logging.info("Found worker name match!")
                        # Tells worker with the same pod name to shutdown
                        worker.register_death()
            worker = Worker(list(map(Queue, listen)), name=worker_name)
            worker.work(with_scheduler=True)
