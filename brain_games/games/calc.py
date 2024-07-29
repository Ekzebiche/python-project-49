from brain_games.common import utils
from colorama import Fore
import prompt


# Скрипт самой игры
def calc_game() -> tuple[str, str]:
    number1, number2 = utils.number_gen(), utils.number_gen()

    operations = ['+', '-', '*']
    operation = utils.random_choose(operations)

    match operation:
        case '+': result = str(number1 + number2)
        case '-': result = str(number1 - number2)
        case '*': result = str(number1 * number2)

    print(f'{Fore.YELLOW}What is the result of the expression?{Fore.RESET}')

    print(
        f'{Fore.YELLOW}Question: {number1} {operation} {number2}{Fore.RESET}')
    answer = prompt.string(f'{Fore.YELLOW} Your answer: {Fore.RESET}').lower()

    return result, answer


def start():
    utils.game_starter(calc_game)
