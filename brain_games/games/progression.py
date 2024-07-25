from brain_games.common import utils


# Скрипт самой игры
def play_progression_game():
    num_start = utils.number_gen(1, 10)
    num_step = utils.number_gen(1, 10)
    num_count = utils.number_gen(5, 15)
    progression, result = utils.make_progression(num_start, num_step, num_count)
    answer = utils.take_progression_answer(progression)
    return result, answer


def start():
    utils.starting_game(play_progression_game, 3)
