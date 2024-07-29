from brain_games.common import utils
from colorama import Fore
import prompt


# Скрипт самой игры
def even_game() -> tuple[str, str]:
    number = utils.number_gen()
    result = 'yes' if number % 2 == 0 else 'no'

    print(
        f'{Fore.YELLOW}'
        'Answer "yes" if the number is even, otherwise answer "no".'
        f'{Fore.RESET}')

    print(f'{Fore.YELLOW}Question: {number}{Fore.RESET}')
    answer = prompt.string(f'{Fore.YELLOW}Your answer: {Fore.RESET}').lower()

    return result, answer if answer in ['yes', 'no'] else None


def start():
    utils.game_starter(even_game)
