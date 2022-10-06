import asyncio
from random import randint


async def draw_lottery_numbers(max, size):
    numbers = set()
    while len(numbers) < size:
        numbers.add(randint(1, max))
    numbers = list(numbers)
    numbers.sort()
    return numbers


async def myapp():
    numbers = await asyncio.gather(draw_lottery_numbers(60, 6), draw_lottery_numbers(50, 5),
                                   draw_lottery_numbers(40, 4))
    print(numbers)


asyncio.run(myapp())
