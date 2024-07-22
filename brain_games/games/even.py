from brain_games.common import utils


# Скрипт самой игры
def play_even_game(name):
    number = utils.number_gen()
    result = utils.check_is_even(number)
    answer = utils.take_even_answer(number)
    utils.check_answer(name, result, answer)


def start():
    name = utils.find_out_name()
    utils.starting_game(name, play_even_game, 3)
