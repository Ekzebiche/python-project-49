from brain_games.common import utils


# Скрипт самой игры
def play_gcd_game():
    number1 = utils.number_gen()
    number2 = utils.number_gen()
    result = utils.count_gcd(number1, number2)
    answer = utils.take_gcd_answer(number1, number2)
    return result, answer


def start():
    utils.starting_game(play_gcd_game, 3)
