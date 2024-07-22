from brain_games.common import utils


# Скрипт самой игры
def play_progression_game(name):
    num_start = utils.number_gen(1, 10)
    num_step = utils.number_gen(1, 10)
    num_count = utils.number_gen(5, 15)
    progression, result = utils.make_progression(num_start, num_step, num_count)
    answer = utils.take_progression_answer(progression)
    utils.check_answer(name, result, answer)


def start():
    name = utils.find_out_name()
    utils.starting_game(name, play_progression_game, 3)
