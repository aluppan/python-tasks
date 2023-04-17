import string
equat = input("Введите арифметическое выражение: ")
symbols = '*/+-'
formula = [(i, equat.index(i)) for i in equat if i in string.digits + symbols]
result = eval(''.join(i[0] for i in formula), {'builtins': None})
print(result)


