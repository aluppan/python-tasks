import random
random_num = random.randint(1, 100)
while True:
    num = int(input())
    result = random_num - num
    if num <= 0 or num > 100:
        print("Число должно быть в диапозоне от 1 до 100")
        continue
    if result > 30:
        print("Очень холодно!")
        continue
    if 20 < result <= 30:
        print("Холодно")
        continue
    if 10 < result <= 20:
        print("Тепло!")
        continue
    if 0 < result <= 10:
        print("Горячо!")
        continue
    if num == random_num:
        print("Вы угадали число!!!")
        break


