from random import randint
import threading
from concurrent.futures.thread import ThreadPoolExecutor

lottery_numbers = []


def draw_lottery_numbers(max, size):
    numbers = set()
    while len(numbers) < size:
        numbers.add(randint(1, max))
    numbers = list(numbers)
    numbers.sort()
    return numbers

"""
threads = []

for i in range(0, 100):
    thread = threading.Thread(target=draw_lottery_numbers, args=(60, 6))
    threads.append(thread)
    thread.start()
"""

futures = []
with ThreadPoolExecutor(max_workers=8) as my_thread_pool:
    for i in range(0, 10000):
        future = my_thread_pool.submit(draw_lottery_numbers, 60, 6)
        futures.append(future)

for future in futures:
    lottery_numbers.append(future.result())

for nums in lottery_numbers:
    print(nums)
