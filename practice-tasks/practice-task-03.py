# #1
# word = input("Введите слово - ")
# if " " in word:
#     print("Введите слово, а не предложение!")
# else:
#     sum = len(word)
#     word1 = word[:sum//2]
#     word2 = word[sum//2:]
#     print(word1, " / ", word2)

# #2
# new_word = input()
# new_word = new_word.replace(".", "")
# new_word = new_word.replace(",", "")
# new_word = new_word.replace("!", "")
# new_word = new_word.replace(":", "")
# new_word = new_word.replace("?", "")
# new_word = new_word.replace(";", "")
# new_word = new_word.replace("'", "")
# new_word = new_word.replace('"', "")
# print(new_word)

#3
new_word = input()
shift = int(input("Cдвинуть на - "))
new_word = new_word[shift:] + new_word[:shift]
print(new_word)

