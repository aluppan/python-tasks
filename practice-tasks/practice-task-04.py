import random
#1
# my_list = [1, 2, 3, 9, 8, 7]
# my_new_list = []
# for i in my_list:
#     my_new_list.append(i * 2)
# print(my_new_list)

#2
# new_list = []
# while True:
#     new_list.append(input())
#     if new_list[-1] == "stop":
#         new_list.pop()
#         break
# print(new_list)

#3
new_list = []
rand = int(input("Ввдедите случайное число от 1 до 10 - "))
for i in range(rand):
    new_list.append(random.randint(1, 10))
print(new_list)