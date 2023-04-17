#1
x = int(input("cislo: "))
y = int(input("kratnoe na: "))
def kratnoe():
    if x % y == 0:
        return print("kratno")
    else:
        return print("ne kratno")
print(kratnoe())

#2, 3
n = int(input("proverka na cetnost"))
def even_odd(n):
    if n % 2 == 0:
        return "even"
    else:
        return "odd"
print(even_odd(n))

#4
import random
_range = int(input("range: "))
def random_dip():
    return [random.randint(-10, 10) for i in range(_range)]
print(random_dip())

# #5
# dlina = input("dlina: ")
# def random_dlina():
#     return ("").join([chr(random.randint(1, 100)) for j in range(dlina)]
# print(random_dlina())