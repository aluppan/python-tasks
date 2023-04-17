# #1
# even_sum = 0
# even_number = 0
# odd_multiply = 1
# odd_number = 0
# while True:
#     number = input()
#     if number == "stop":
#         break
#     number = int(number)
#     if number % 2 == 0:
#         even_sum += number
#         even_number += 1
#     if number % 2 != 0:
#         odd_multiply *= number
#         odd_number += 1
# print("Сумму чётных чисел - ", even_sum)
# print("Произведение нечётных чисел - ", odd_multiply)
# print("Среднее арифметическое для чётных чисел - ", even_sum / even_number)
# print("Среднее арифметическое для нечётных чисел - ", odd_multiply / odd_number)

#2
while True:
    print("")
    print("Календарь апрель 2021 года")
    days = int(input("Введите день - "))
    if days <= 0 or days >= 31:
        print("В апреле 30 дней!")
        continue
    if days == 5 or days == 12 or days == 19 or days == 26:
        print(f"{days} апреля это Понедельник!")
        continue
    if days == 6 or days == 13 or days == 20 or days == 27:
        print(f"{days} апреля это Вторник!")
        continue
    if days == 7 or days == 14 or days == 21 or days == 28:
        print(f"{days} апреля это Среда!")
        continue
    if days == 1 or days == 8 or days == 15 or days == 22 or days == 29:
        print(f"{days} апреля это Четверг!")
        continue
    if days == 2 or days == 9 or days == 16 or days == 23 or days == 30:
        print(f"{days} апреля это Пятница!")
        continue
    if days == 3 or days == 10 or days == 17 or days == 24:
        print(f"{days} апреля это Суббота!")
        continue
    if days == 4 or days == 11 or days == 18 or days == 25:
        print(f"{days} апреля это Воскресенье!")
        continue