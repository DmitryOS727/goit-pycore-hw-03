import random

def get_numbers_ticket(min, max, quantity):
    if min < 1 or max > 1000 or min > max:
        return[] # Перевірка на правильність введених даних
    numbers = set()
    while len(numbers) < quantity:
        random_number = random.randint(min, max) # Генерація випадкового числа в діапазоні від min до max
        numbers.add(random_number)
    result = sorted(numbers) # Сортування чисел за зростанням
    return result
lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Ваші лотерейні числа:", lottery_numbers)