import logging
import os
import threading
import time

print(f"# of logical processors is {os.cpu_count()}")

data = 0


def task(name):
    global data  # process
    print(f"Thread {name} has just started.")
    for i in range(0, 500000):
        # time.sleep(delay)
        data += 1
        # logging.info(f"Thread {name} is running for {count} time...")
    print(f"Thread {name} has just finished.")


logging.basicConfig(format="%(asctime)s: %(message)s", level=logging.INFO, datefmt="%H:%M:%S")

threads = []
for i in range(0, 16):
    t = threading.Thread(target=task, args=(f"Thread #{i + 1}",))
    t.start()
    threads.append(t)

for t in threads:
    t.join()
logging.info(f"data: {data}")
logging.info("application is done.")
