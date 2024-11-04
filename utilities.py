# Створіть власний Python-модуль з ім'ям `utilities.py`. У цьому модулі створіть наступні функції:

# 1. `calculate_average(numbers)`: Приймає список чисел `numbers` і повертає середнє арифметичне цих чисел.
# 2. `find_max(numbers)`: Приймає список чисел `numbers` і повертає найбільше число у списку.

# Після створення цього модуля, створіть інший Python-файл (наприклад, `main.py`), 
# який імпортує модуль `utilities.py` і використовує його функції для обробки списку чисел.

# В `main.py` створіть список чисел та використовуйте функції з модуля `utilities` 
# для знаходження середнього значення та найбільшого числа у списку. Виведіть результати на екран.

def calculate_average(numbers):
    total = 0
    for number in numbers:
        total = total + number
    average = total / len(numbers)
    print(f"Average of {numbers}: {average}")
    return average

# def find_max(numbers):
#     result = max(numbers)
#     print(f"Max: {result}")
#     return result

def find_max(numbers):
    max_number = numbers[0]
    for number in numbers:
        if max_number < number:
            max_number = number

    print(f"Max of {numbers}: {max_number}")
    return max_number

numbers_01 = [-10, -7, -31, -4, -5, -22, -17, -54, -3, -11]
numbers_02 = [10, 7, 31, 4, 5, 22, 17, 54, 3, 11]

find_max(numbers_01)
find_max(numbers_02)

calculate_average(numbers_01)
calculate_average(numbers_02)
