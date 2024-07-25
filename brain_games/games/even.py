from brain_games.common import utils


# Скрипт самой игры
def play_even_game():
    number = utils.number_gen()
    result = utils.check_is_even(number)
    answer = utils.take_even_answer(number)
    return result, answer


def start():
    utils.starting_game(play_even_game, 3)
