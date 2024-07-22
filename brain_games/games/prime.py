from brain_games.common import utils


# Скрипт самой игры
def play_prime_game(name):
    number = utils.number_gen()
    result = utils.check_is_prime(number)
    answer = utils.take_even_answer(number)
    utils.check_answer(name, result, answer)


def start():
    name = utils.find_out_name()
    utils.starting_game(name, play_prime_game, 3)
