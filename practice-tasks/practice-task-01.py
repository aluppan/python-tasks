import math
a = float(input("a - "))
b = float(input("b - "))
c = float(input("c - "))
d = b ** 2 - 4 * a * c
print("Дискриминант - ", d)
if d > 0:
    x1 = (-b + math.sqrt(d)) / (2 * a)
    x2 = (-b - math.sqrt(d)) / (2 * a)
    print("x1 - ", round(x1, 2))
    print("x2 - ", round(x2, 2))
elif d == 0:
    x = -b / (2 * a)
    print("x - ", x)
else:
    print("Корней нет")
