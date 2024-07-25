import prompt
import random
import math
import gmpy2
from colorama import Fore


# Запрос имени
def find_out_name():
    print(f'{Fore.GREEN}Welcome to the Brain Games!{Fore.RESET}')
    name = prompt.string(f'{Fore.YELLOW}May I have your name? {Fore.RESET}')
    print(f'{Fore.GREEN}Hello, {name}!{Fore.RESET}')
    return name


# Генерация числа, с учетом, его уникальности в последующих итерациях.
# Чтобы не выпадали повторения.
def number_gen(start=1, end=100):
    number = random.randint(start, end)
    return number


# Случайный выбор математического действия
def choose_operation():
    operations = ['+', '-', '*']
    operation = random.choice(operations)
    return operation


# Проверка на четность
def check_is_even(number):
    return 'yes' if number % 2 == 0 else 'no'


# Проверка на простое
def check_is_prime(number):
    return 'yes' if gmpy2.is_prime(number) is True else 'no'


# Проверка на число
def check_is_integer(data):
    try:
        if int(data):
            return int(data)
    except ValueError:
        return None
    return None


# Вычисление математического выражения
def count_calc_expression(number1, number2, operation):
    match operation:
        case '+':
            result = number1 + number2
        case '-':
            result = number1 - number2
        case '*':
            result = number1 * number2

    return result


# Вычисление НАИБОЛЬШЕГО ДЕЛИТЕЛЯ
def count_gcd(number1, number2):
    result = math.gcd(number1, number2)
    return result


# Создание листа арифметической прогрессии
def make_progression(start, step, count):
    progression = list(range(start, start + step * count, step))
    random_num = random.choice(progression)
    index = progression.index(random_num)
    progression[index] = '..'
    progression_str = ' '.join(map(str, progression))
    return progression_str, random_num


# Получение ответа для игры в ЧЕТНОЕ с приведением к регистру
def take_even_answer(number):
    print(
        f'{Fore.YELLOW}'
        'Answer "yes" if the number is even, otherwise answer "no".'
        f'{Fore.RESET}')

    print(f'{Fore.YELLOW}Question: {number}{Fore.RESET}')

    answer = prompt.string(f'{Fore.YELLOW}Your answer: {Fore.RESET}').lower()

    return answer if answer in ['yes', 'no'] else None


# Получение ответа для игры в ПРОСТОЕ с приведением к регистру
def take_prime_answer(number):
    print(
        f'{Fore.YELLOW}'
        'Answer "yes" if given number is prime. Otherwise answer "no".'
        f'{Fore.RESET}')

    print(f'{Fore.YELLOW}Question: {number}{Fore.RESET}')

    answer = prompt.string(f'{Fore.YELLOW}Your answer: {Fore.RESET}').lower()

    return answer if answer in ['yes', 'no'] else None


# Получение ответа для КАЛЬКУЛЯТОРА
def take_calc_answer(number1, number2, operation):
    print(f'{Fore.YELLOW}What is the result of the expression?{Fore.RESET}')
    print(
        f'{Fore.YELLOW}'
        f'Question: {number1} {operation} {number2}'
        f'{Fore.RESET}')

    answer = check_is_integer(prompt.string(
        f'{Fore.YELLOW}'
        'Your answer: '
        f'{Fore.RESET}'
    ))

    return answer


# Получение ответа для НАИБОЛЬШЕГО ДЕЛИТЕЛЯ
def take_gcd_answer(number1, number2):
    print(
        f'{Fore.YELLOW}'
        'Find the greatest common divisor of given numbers.'
        f'{Fore.RESET}')

    print(f'{Fore.YELLOW}Question: {number1} {number2}{Fore.RESET}')

    answer = check_is_integer(prompt.string(
        f'{Fore.YELLOW}'
        'Your answer: '
        f'{Fore.RESET}'
    ))

    return answer


# Получение ответа для ПРОГРЕССИИ
def take_progression_answer(prog_list):
    print(
        f'{Fore.YELLOW}'
        'What number is missing in the progression?'
        f'{Fore.RESET}')

    print(f'{Fore.YELLOW}Question: {prog_list}{Fore.RESET}')

    answer = check_is_integer(prompt.string(
        f'{Fore.YELLOW}'
        'Your answer: '
        f'{Fore.RESET}'
    ))

    return answer


# Проверка ответа
def check_answer(name, result, answer):
    if answer == result:
        print(f'{Fore.GREEN}Correct!{Fore.RESET}')
        return True

    elif answer is None:
        print(
            f'{Fore.RED}'
            f'{name}, the answer is not in the game format. Try again!'
            f'{Fore.RESET}')
        return False

    else:
        print(
            f'{Fore.RED}'
            f'"{answer}" is wrong answer ;(. Correct answer was "{result}".'
            f'{Fore.RESET}')

        print(f'{Fore.RED}Let\'s try again, {name}!{Fore.RESET}')
        return False


# Скрипт запуска игры, с учетом количества ее итераций
def starting_game(game, count):

    game_count = 0
    answers = []

    name = find_out_name()

    while game_count < count:
        result, answer = game()
        i = check_answer(name, result, answer)

        if i is True:
            answers.append(i)
        else:
            break

        game_count += 1

    if len(answers) == 3:
        print(f'{Fore.GREEN}Congratulations, {name}!{Fore.RESET}')
