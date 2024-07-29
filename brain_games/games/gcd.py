from brain_games.common import utils
from colorama import Fore
import prompt
import math


# Скрипт самой игры
def gcd_game() -> tuple[str, str]:
    number1 = utils.number_gen()
    number2 = utils.number_gen()
    result = str(math.gcd(number1, number2))

    print(
        f'{Fore.YELLOW}'
        'Find the greatest common divisor of given numbers.'
        f'{Fore.RESET}')

    print(f'{Fore.YELLOW}Question: {number1} {number2}{Fore.RESET}')
    answer = prompt.string(f'{Fore.YELLOW}Your answer: {Fore.RESET}').lower()

    return result, answer


def start():
    utils.game_starter(gcd_game)
