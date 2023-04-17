#1
# word = input()
# user_range_1 = int(input())
# user_range_2 = int(input())
# first_letter = word[0]
# shear = word[user_range_1:user_range_2:1]
# if user_range_1 == 0:
#     print(word[user_range_1:user_range_2] + shear[::-1] + word[user_range_2:])
# else:
#     print(first_letter + word[user_range_1:user_range_2] + shear[::-1] + word[user_range_2:])



#2
# while True:
#     word1 = input()
#     up_1 = input()
#     word1 = word1.replace(up_1, up_1.upper())
#     print(word1)
#     break


#3.0
# num_val = float(input())
# val1 = input("Выберите валюту: RUB, AZN, EUR, USD ")
# if val1 == 'RUB':
#     sum1 = num_val * 0.023
#     print("RUB to AZN - ", sum1)
#     sum2 = num_val * 0.011
#     print("RUB to EUR - ", sum2)
#     sum3 = num_val * 0.013
#     print("RUB to USD - ", sum3)
# if val1 == 'AZN':
#     sum1 = num_val * 43.35
#     print("AZN to RUB - ", sum1)
#     sum2 = num_val * 0.48
#     print("AZN to EUR - ", sum2)
#     sum3 = num_val * 0.58
#     print("AZN to USD - ", sum3)
# if val1 == 'EUR':
#     sum1 = num_val * 90.02
#     print("EUR to RUB - ", sum1)
#     sum2 = num_val * 2.07
#     print("EUR to AZN - ", sum2)
#     sum3 = num_val * 1.22
#     print("EUR to USD - ", sum3)
# if val1 == 'USD':
#     sum1 = num_val * 73.65
#     print("USD to RUB - ", sum1)
#     sum2 = num_val * 1.70
#     print("USD to AZN - ", sum2)
#     sum3 = num_val * 0.81
#     print("USD to EUR - ", sum3)

#3.1
# num_val = float(input("Введите сумму - "))
# val1 = input("Выберите валюту: RUB, AZN, EUR, USD ")
# val2 = input("Выберите вторую валюту: RUB, AZN, EUR, USD ")
# if val1 == 'RUB' and val2 == 'AZN':
#     sum = num_val * 0.023
#     print(sum)
# if val1 == 'RUB' and val2 == 'EUR':
#     sum = num_val * 0.011
#     print(sum)
# if val1 == 'RUB' and val2 == 'USD':
#     sum = num_val * 0.013
#     print(sum)
#
# if val1 == 'AZN' and val2 == 'RUB':
#     sum1 = num_val * 43.35
#     print("AZN to RUB - ", sum1)
# if val1 == 'AZN' and val2 == 'EUR':
#     sum2 = num_val * 0.48
#     print("AZN to EUR - ", sum2)
# if val1 == 'AZN' and val2 == 'USD':
#     sum3 = num_val * 0.58
#     print("AZN to USD - ", sum3)
#
# if val1 == 'EUR' and val2 == 'RUB':
#     sum1 = num_val * 90.02
#     print("EUR to RUB - ", sum1)
# if val1 == 'EUR' and val2 == 'EUR':
#     sum2 = num_val * 2.07
#     print("EUR to AZN - ", sum2)
# if val1 == 'EUR' and val2 == 'USD':
#     sum3 = num_val * 1.22
#     print("EUR to USD - ", sum3)
#
# if val1 == 'USD' and val2 == 'RUB':
#     sum1 = num_val * 73.65
#     print("USD to RUB - ", sum1)
# if val1 == 'USD' and val2 == 'AZN':
#     sum2 = num_val * 1.70
#     print("USD to AZN - ", sum2)
# if val1 == 'USD' and val2 == 'EUR':
#     sum3 = num_val * 0.81
#     print("USD to EUR - ", sum3)