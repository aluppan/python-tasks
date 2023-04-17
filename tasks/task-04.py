#Задание 1
#Сумма
# begin = int(input("Begin - "))
# end = int(input("End - "))
# sum = 0
# while begin <= end:
#     sum += begin
#     begin += 1
# print(sum)

#Произведение
# begin1 = int(input("Begin - "))
# end1 = int(input("End - "))
# multiply = 1
# while begin1 <= end1:
#     multiply *= begin1
#     begin1 += 1
# x = 1
# res = 0
# while multiply:
#     multiply, zero = divmod(multiply, 10)
#     if zero != 0:
#         res += zero * x
#         x *= 10
# print(res)

#Произведение только нечётных чисел
# begin2 = int(input("Begin - "))
# end2 = int(input("End - "))
# multiply2 = 1
# while begin2 <= end2:
#     if begin2 % 2 != 0 and begin2 % 3 != 0:
#         multiply2 *= begin2
#     begin2 += 1
# print(multiply2)

#Задание 2
max = 0
min = 0
arithmetic = 0
quantity = 0
negative = False
while True:
    num = input()
    if num == "stop":
        break
    num = int(num)
    if num % 7 == 0:
        continue
    quantity += 1
    arithmetic += int(num)
    if not negative:
        max = min = num
        negative = True
        continue
    if max < num:
        max = num
    if min > num:
        min = num
print("max - ", max)
print("min - ", min)
print("arithmetic mean - ", arithmetic / quantity)

