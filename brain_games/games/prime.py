from brain_games.common import utils


# Скрипт самой игры
def play_prime_game():
    number = utils.number_gen()
    result = utils.check_is_prime(number)
    answer = utils.take_prime_answer(number)
    return result, answer


def start():
    utils.starting_game(play_prime_game, 3)
