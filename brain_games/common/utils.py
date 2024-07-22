import prompt
import random
import math
from sympy import isprime
from colorama import Fore


# Запрос имени
def find_out_name():
    print(Fore.GREEN + 'Welcome to the Brain Games!' + Fore.RESET)
    name = prompt.string(Fore.YELLOW + 'May I have your name? ' + Fore.RESET)
    print(Fore.GREEN + f'Hello, {name}!' + Fore.RESET)
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
    return 'yes' if isprime(number) is True else 'no'


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
    return progression, random_num


# def ask_question(game):
#     questions = {
#         'even': 'Answer "yes" if the number is even, otherwise answer "no".',
#         'prime': 'Answer "yes" if the number is even, otherwise answer "no".',
#         'calc': 'What is the result of the expression?',
#         'gcd': 'Find the greatest common divisor of given numbers.',
#         'prog': 'What number is missing in the progression?'
#     }
#     print(Fore.YELLOW + questions[f'{game}'] + Fore.RESET)


# Получение ответа для игры в ЧЕТНОЕ с приведением к регистру
def take_even_answer(number):
    print(Fore.YELLOW + 'Answer "yes" if the number is even, otherwise answer "no".' + Fore.RESET)
    print(Fore.YELLOW + f'Question: {number}' + Fore.RESET)

    answer = prompt.string(Fore.YELLOW + 'Your answer: ' + Fore.RESET).lower()

    return answer if answer in ['yes', 'no'] else None


# Получение ответа для игры в ПРОСТОЕ с приведением к регистру
def take_prime_answer(number):
    print(Fore.YELLOW + 'Answer "yes" if given number is prime. Otherwise answer "no".' + Fore.RESET)
    print(Fore.YELLOW + f'Question: {number}' + Fore.RESET)

    answer = prompt.string(Fore.YELLOW + 'Your answer: ' + Fore.RESET).lower()

    return answer if answer in ['yes', 'no'] else None


# Получение ответа для КАЛЬКУЛЯТОРА
def take_calc_answer(number1, number2, operation):
    print(Fore.YELLOW + 'What is the result of the expression?' + Fore.RESET)
    print(Fore.YELLOW + f'Question: {number1} {operation} {number2}' + Fore.RESET)

    answer = check_is_integer(prompt.string(Fore.YELLOW + 'Your answer: ' + Fore.RESET))

    return answer


# Получение ответа для НАИБОЛЬШЕГО ДЕЛИТЕЛЯ
def take_gcd_answer(number1, number2):
    print(Fore.YELLOW + 'Find the greatest common divisor of given numbers.' + Fore.RESET)
    print(Fore.YELLOW + f'Question: {number1} {number2}' + Fore.RESET)

    answer = check_is_integer(prompt.string(Fore.YELLOW + 'Your answer: ' + Fore.RESET))

    return answer


# Получение ответа для ПРОГРЕССИИ
def take_progression_answer(prog_list):
    print(Fore.YELLOW + 'What number is missing in the progression?' + Fore.RESET)
    print(Fore.YELLOW + f'Question: {prog_list}' + Fore.RESET)

    answer = check_is_integer(prompt.string(Fore.YELLOW + 'Your answer: ' + Fore.RESET))

    return answer


# Проверка ответа
def check_answer(name, result, answer):
    if answer == result:
        print(Fore.GREEN + 'Correct!' + Fore.RESET)

    elif answer is None:
        print(Fore.RED + f'{name}, the answer is not in the game format. Try again!' + Fore.RESET)

    else:
        print(Fore.RED + f'"{answer}" is wrong answer ;(. Correct answer was "{result}".' + Fore.RESET)
        print(Fore.RED + f'Let\'s try again, {name}' + Fore.RESET)


# Скрипт запуска игры, с учетом количества ее итераций
def starting_game(name, game, count):
    game_count = 0

    while game_count < count:
        game(name)
        game_count += 1
