import random
n = int(input("Введите диапазон рандомных чисел: "))
begin = int(input("Начало: "))
end = int(input("Конец: "))
_list = [random.randint(begin, end) for _ in range(n)]
print("список случайных чисел - ", _list)
even_numbers = [number for number in _list if number % 2 == 0]
odd_numbers = [number for number in _list if number % 2 != 0]
negative_numbers = [number for number in _list if number < 0]
positive_numbers = [number for number in _list if number > 0]
print("четные числа - ", even_numbers)
print("нечетные числа - ", odd_numbers)
print("отрицательные числа - ", negative_numbers)
print("положительные числа - ", positive_numbers)