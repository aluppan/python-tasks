# #Задание 1
# num = int(input("number "))
# if num % 2 == 0:
#     print("even")
# else:
#     print("odd")

#Задание 2
# num1 = int(input("num1 "))
# num2 = int(input("num2 "))
# num3 = int(input("num3 "))
# num4 = int(input("num4 "))
# num5 = int(input("num5 "))
# max = num1
# min = num1
# if max < num2:
#     max = num2
# if max < num3:
#     max = num3
# if max < num4:
#     max = num4
# if max < num5:
#     max = num5
# if min > num2:
#     min = num2
# if min > num3:
#     min = num3
# if min > num4:
#     min = num4
# if min > num5:
#     min = num5
# print("max", max)
# print("min", min)

#Задание 3
# num6 = input()
# select = input("select bool, int, float ")
# if select == 'bool':
#     print(bool(num6))
# if select == 'int':
#     print(int(num6))
# if select == 'float':
#     print(float(num6))
# select = input("select new bool, int, float ")
# if select == 'bool':
#     print(bool(num6))
# if select == 'int':
#     print(int(num6))
# if select == 'float':
#     print(float(num6))


#Задание 4
num7 = int(input("num1 "))
num8 = int(input("num2 "))
sum = input("select | + | - | * | / | // | % | ** | & | ")
if sum == "+":
    print(num7 + num8)
if sum == "-":
    print(num7 - num8)
if sum == "*":
    print(num7 * num8)
try:
    if sum == "/":
        print(num7 / num8)
except ZeroDivisionError:
    print("cannot be divided by zero")
if sum == "//":
    print(num7 // num8)
if sum == "%":
    print(num7 % num8)
if sum == "**":
    print(num7 ** num8)
if sum == "&":
    print(num7 ** 0.5, num8 ** 0.5)

