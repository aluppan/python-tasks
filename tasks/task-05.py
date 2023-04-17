# #1
# for i in range(1):
#     symbol1 = input("Символ - ")
#     range1 = int(input("Длина - "))
#     if range1 < 3 or range1 > 15:
#         print("Длина меньше 3 или больше 15")
#         break
#     print("Чтобы выбрать Горизонтально нажмите 1")
#     print("Чтобы выбрать Вертикально нажмите 2")
#     print("Чтобы выбрать По диагонали нажмите 3")
#     direction = int(input())
#     if direction != 1 and direction != 2 and direction != 3:
#         print("Ошибка! Введите число в диапазоне от 1 до 3")
#         break
#     if direction == 1:
#         for a in range(range1):
#             print(symbol1, end='')
#     if direction == 2:
#         for b in range(range1):
#             print(symbol1)
#     if direction == 3:
#         for c in range(range1):
#             for d in range(range1):
#                 if c == d:
#                     print(symbol1, end='')
#                 else:
#                     print(' ', end='')
#             print()

# #2
# num = int(input("Введите число - "))
# begin_range = int(input("Начало диапазона - "))
# end_range = int(input("Конец диапазона - "))
# for a in range(1):
#     if begin_range > end_range:
#         print("Начало диапазона больше конца!")
#         break
#     for i in range(begin_range, end_range + 1):
#         res = num ** i
#         print(res)

# #3
# multi_begin_range = int(input("Начало диапазона множимого - "))
# multi_end_range = int(input("Конец диапазона множимого - "))
# factor_begin_range = int(input("Начало диапазона множителя - "))
# factor_end_range = int(input("Конец диапазона множителя - "))
# for a in range(1):
#     if multi_begin_range == 0 or multi_end_range == 0 or factor_begin_range == 0 or factor_end_range == 0:
#         print("В диапазоне есть ноль")
#         break
#     if multi_begin_range > multi_end_range or factor_begin_range > factor_end_range:
#         print("Начало диапазона больше конца!")
#         break
#     for i in range(multi_begin_range, multi_end_range + 1):
#         for j in range(factor_begin_range, factor_end_range + 1):
#             res = i * j
#             print(res)