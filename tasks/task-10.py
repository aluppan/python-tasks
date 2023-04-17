text = str(input("Введите текст транслитом, чтобы преобразовать в русский язык - "))

alphabet = {'a': 'а', 'b': 'б', 'v': 'в', 'g': 'г', 'd': 'д', 'e': 'е', 'j': 'ж', 'z': 'з',
            'i': 'и', 'y': 'й', 'k': 'к', 'l': 'л', 'm': 'м', 'n': 'н', 'o': 'о', 'p': 'п',
            'r': 'р', 's': 'с', 't': 'т', 'u': 'у', 'f': 'ф', 'h': 'x', 'c': 'ц',
            'A': 'А', 'B': 'Б', 'V': 'В', 'G': 'Г', 'D': 'Д', 'E': 'Е', 'J': 'Ж', 'Z': 'З',
            'I': 'И', 'Y': 'Й', 'K': 'К', 'L': 'Л', 'M': 'М', 'N': 'Н', 'O': 'О', 'P': 'П',
            'R': 'Р', 'S': 'С', 'T': 'Т', 'U': 'У', 'F': 'Ф', 'H': 'Х', 'C': 'Ц'}

for i in alphabet:
    for j in text:
        text = text.replace("Yu", "Ю")
        text = text.replace("yu", "ю")
        text = text.replace("Ya", "Я")
        text = text.replace("ya", "я")
        text = text.replace("Ch", "Ч")
        text = text.replace("ch", "ч")
        text = text.replace("Ey", "Э")
        text = text.replace("ey", "э")
        text = text.replace("Sh", "Ш")
        text = text.replace("sh", "ш")
        text = text.replace("Yo", "Ё")
        text = text.replace("yo", "ё")
    text = text.replace(i, alphabet[i])

print(text)

