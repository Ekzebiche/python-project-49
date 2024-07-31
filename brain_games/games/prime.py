from brain_games.common import number_gen, game_starter
from colorama import Fore
import prompt
import gmpy2


# Скрипт самой игры
def prime_game() -> tuple[str, str]:
    number = number_gen()
    result = 'yes' if gmpy2.is_prime(number) is True else 'no'

    print(
        f'{Fore.YELLOW}'
        'Answer "yes" if given number is prime. Otherwise answer "no".'
        f'{Fore.RESET}')

    print(f'{Fore.YELLOW}Question: {number}{Fore.RESET}')
    answer = prompt.string(f'{Fore.YELLOW}Your answer: {Fore.RESET}').lower()

    return result, answer if answer in ('yes', 'no') else None


def start() -> None:
    game_starter(prime_game)
