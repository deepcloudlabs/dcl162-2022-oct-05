import logging
import os
from threading import Lock, Thread

logging.basicConfig(format="%(asctime)s: %(message)s", level=logging.INFO, datefmt="%H:%M:%S")
logging.info(f"# of logical processors is {os.cpu_count()}")

data = 0

lock = Lock()


def task(name):
    global data
    logging.info(f"Thread {name} has just started.")
    with lock:
        for i in range(0, 5000):
            # time.sleep(delay)
            local = data
            local += 1
            logging.info(f"Thread {name} is running for {i + 1} time...")
            data = local
    logging.info(f"Thread {name} has just finished.")


threads = []
for i in range(0, os.cpu_count()):
    t = Thread(target=task, args=(f"Thread #{i + 1}",))
    t.start()
    threads.append(t)

for t in threads:
    t.join()
logging.info(f"data: {data}")
logging.info("application is done.")
