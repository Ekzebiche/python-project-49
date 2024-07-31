import prompt
from colorama import Fore


def game_starter(game=None, count=3) -> None:
    game_count = 0
    answers = []

    print(f'{Fore.GREEN}Welcome to the Brain Games!{Fore.RESET}')
    name = prompt.string(f'{Fore.YELLOW}May I have your name? {Fore.RESET}')
    print(f'{Fore.GREEN}Hello, {name}!{Fore.RESET}')

    if game is not None:

        while game_count < count:
            result, answer = game()

            if answer == result:
                print(f'{Fore.GREEN}Correct!{Fore.RESET}')
                answers.append(True)

            elif answer is None:
                print(
                    f'{Fore.RED}'
                    f'{name}, the answer is not in the game format. Try again!'
                    f'{Fore.RESET}')
                break

            else:
                print(
                    f'{Fore.RED}'
                    f'"{answer}" is wrong answer ;(.'
                    f'Correct answer was "{result}".'
                    f'{Fore.RESET}')

                print(f'{Fore.RED}Let\'s try again, {name}!{Fore.RESET}')
                break

            game_count += 1

        if len(answers) == 3:
            print(f'{Fore.GREEN}Congratulations, {name}!{Fore.RESET}')
