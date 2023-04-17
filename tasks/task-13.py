
#1
num1 = int(input())
num2 = int(input())
num3 = int(input())
num4 = int(input())

def max_num():
    if num1 > num2 and num1 > num3 and num1 > num4:
        return num1
    if num2 > num1 and num2 > num3 and num2 > num4:
        return num2
    if num3 > num1 and num3 > num2 and num3 > num4:
        return num3
    if num4 > num1 and num4 > num3 and num4 > num2:
        return num4
def min_num():
    if num1 < num2 and num1 < num3 and num1 < num4:
        return num1
    if num2 < num1 and num2 < num3 and num2 < num4:
        return num2
    if num3 < num1 and num3 < num2 and num3 < num4:
        return num3
    if num4 < num1 and num4 < num3 and num4 < num2:
        return num4
print(f"MAX - {max_num()}")
print(f"MIN - {min_num()}")

#2
num5 = int(input())
num6 = int(input())
def odd_num():
    for i in range(num5, num6 + 1):
        return [x for x in range(num5, num6 + 1) if x % 2 == 0]
print(odd_num())

#3
num7 = int(input())
num8 = int(input())

def sum_num():
    sum = 0
    for x in range(num7, num8 + 1):
        sum += x
    return sum
print(sum_num())