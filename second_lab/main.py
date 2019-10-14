"""
NNSTU IRIT 16-V-2
Student: Shunin Kirill
1 10 2019
"""
# coding=utf-8
import RC4

n = 12
key = '12345'

with open('text.txt', 'r', encoding='utf-8') as input_data:
    # Открываем исходный файл и записываем данные из него в переменную data.
    data = input_data.read()

# Генерируем ключевой поток и шифруем исходные данные
s_block = RC4.s_block_generate(data, key, n)
encoded_data = RC4.encode(data, s_block)

with open('encoded.txt', 'w', encoding='utf-8') as out_data:
    # Выводим шифр в файл encoded.txt
    for element in encoded_data:
        out_data.write(str(element) + ' ')

with open('encoded.txt', 'r', encoding='utf-8') as inpt_data:
    # Открываем файл с шифром и записываем данные из него в переменную data.
    data = inpt_data.read().split()

# Повторно генерируем ключевой поток и расшифровываем данные.
s_block = RC4.s_block_generate(data, key, n)
decoded_data = RC4.decode(data, s_block)

with open('decoded.txt', 'w', encoding='utf-8') as out_data:
    # Записываем результат в decoded.txt
    for element in decoded_data:
        out_data.write(element)
