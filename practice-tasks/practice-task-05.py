import random
#1
_list = [random.randint(-10, 10) for _ in range(10)]
print("Список случайных чисе: ", _list, "\n")
negative_sum = 0
for number in _list:
    if number < 0:
        negative_sum += number
print("Сумму отрицательных чисел: ", negative_sum)

#2
even_sum = 0
for number in _list:
    if number % 2 == 0:
        even_sum += number
print("Сумму четных чисел: ", even_sum)

#3
odd_sum = 0
for number in _list:
    if number % 2 != 0:
        odd_sum += number
print("Сумму нечетных чисел: ", odd_sum)

#4
multi_3_sum = 1
for number in _list:
    if number % 3 == 0:
        multi_3_sum *= number
print("Произведение элементов с индексами кратными 3 - ", multi_3_sum)




