# 1
# word = str(input("Введите слово - "))
# if " " in word:
#     print("Введите слово, а не предложение!")
# else:
#     new_word = word[::-1]
#     print(new_word)

# #2
# word = str(input("Введите строки - "))
# new_word = word[::-1]
# print(new_word)

# #3
# word = input("Введите строки - ")
# word = word.lower()
# glasn = ['а', 'у', 'о', 'ы', 'и', 'э', 'я', 'ю', 'ё', 'е']
# soglasn = ['б', 'в', 'г', 'д', 'ж', 'з', 'й', 'к', 'л', 'м', 'н', 'п', 'р', 'с', 'т', 'ф', 'х', 'ц', 'ч', 'ш', 'щ']
# cisla = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# glasn_kol = 0
# soglasn_kol = 0
# cisla_kol = 0
# for text in word:
#     for i in glasn:
#         if text == i:
#             glasn_kol += 1
#     for i in soglasn:
#         if text == i:
#             soglasn_kol += 1
#     for i in cisla:
#         if text == i:
#             cisla_kol += 1
# print(f"В вашей строке {cisla_kol} чисел, {glasn_kol} гласных и {soglasn_kol} согласных букв")


# #4
# word = str(input("Введите слово - "))
# sum = len(word)
# if len(word) % 2 == 0:
#     word1 = word[:sum // 2]
#     word2 = word[sum // 2:]
# else:
#     word1 = word[:sum // 2]
#     word2 = word[sum // 2 + 1:]
# word3 = word1[::-1]
# word4 = word2[::-1]
# print(word3 + word4)


# #5
# word = str(input())
# palid = word[::-1]
# if word == palid:
#   print("Палиндром")
# else:
#   print("Не палиндром")
