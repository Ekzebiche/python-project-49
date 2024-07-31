import random


def number_gen(start=1, end=100) -> int:
    return random.randint(start, end)


def random_choose(data) -> str:
    return str(random.choice(data))
