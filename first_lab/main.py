"""
NNSTU IRIT 16-V-2
Student: Shunin Kirill
11 09 2019
"""
from collections import Counter
#алфавит строчных и заглавных букв
ru_alph = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
RU_alph = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
#fixed
#функция кодирования кодом Цезаря
def encode(file, shift, write_file = True):
    """
    :param file: имя файла с текстом для закодирования
    :param shift: смещение
    :param write_file: флаг для записи закодированного текста в файл encoded.txt
    :return: закодированная строка, если write_file = False
    """
    #чтение файла с текстом
    text = ""
    for line in open(file, 'r', encoding='utf-8'):
        text = text + line
    #реализация кода Цезаря
    out = ""
    for i in text:
        if i in ru_alph: #обработка прописных букв
            out = out + ru_alph[(ru_alph.index(i) + shift) % len(ru_alph)]
        elif i in RU_alph: #обработка заглавных букв
            out = out + RU_alph[(RU_alph.index(i) + shift) % len(RU_alph)]
        else: #обработка прочих символов
            out = out + i
    if write_file: #запись в файл, по-умолчанию
        open('encoded.txt', 'w', encoding='utf-8').write(out)
    else: #возвращение строки в другом случае
        return out
#функция декодирования частотным методом
def decode(file, write_file = True):
    """
    :param file: имя файла с текстом для декодирования
    :param write_file: флаг для записи декодированного текста в файл decoded.txt
    :return: декодированная строка, если write_file = False
    """
    #чтение файла с текстом
    text = ""
    for line in open(file, 'r', encoding='utf-8'):
        text = text + line
    #удаление пробелов и приведение к нижнему регистру
    for_most = text.split()
    for_most = ''.join(for_most)
    for_most.lower()
    #вычисление наиболее популярного символа
    c = Counter(for_most)
    most = c.most_common()[0][0]
    #вычисление смещения относительно самого популярного символа в русском языке
    shift = ru_alph.index('о') - ru_alph.index(most)
    #декодирование текста
    decoded = encode(file,shift,False)
    if write_file: #запись в файл, по-умолчанию
        open('decoded.txt', 'w', encoding='utf-8').write(decoded)
    else: #возвращение строки в другом случае
        return decoded
#использование функций
encode("text.txt",2)
decode("encoded.txt")
