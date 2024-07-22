from brain_games.common import utils


# Скрипт самой игры
def play_calc_game(name):
    number1 = utils.number_gen()
    number2 = utils.number_gen()
    result = utils.count_gcd(number1, number2)
    answer = utils.take_gcd_answer(number1, number2)
    utils.check_answer(name, result, answer)


def start():
    name = utils.find_out_name()
    utils.starting_game(name, play_calc_game, 3)
