from brain_games.common import random_choose, number_gen, game_starter
from colorama import Fore
import prompt


# Скрипт самой игры
def progression_game() -> tuple[str, str]:
    start = number_gen(1, 10)
    step = number_gen(1, 10)
    count = number_gen(5, 15)
    progression = list(range(start, start + step * count, step))

    result = random_choose(progression)
    index = progression.index(int(result))
    progression[index] = '..'
    prog_list = ' '.join(map(str, progression))

    print(
        f'{Fore.YELLOW}'
        'What number is missing in the progression?'
        f'{Fore.RESET}')

    print(f'{Fore.YELLOW}Question: {prog_list}{Fore.RESET}')

    answer = prompt.string(
        f'{Fore.YELLOW}Your answer: {Fore.RESET}').lower()

    return result, answer


def start() -> None:
    game_starter(progression_game)
