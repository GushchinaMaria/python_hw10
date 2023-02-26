"""
Задание 3.

Определить, какие из слов «attribute», «класс», «функция», «type»
невозможно записать в байтовом типе с помощью маркировки b'' (без encode decode).

Подсказки:
--- используйте списки и циклы, не дублируйте функции
--- обязательно!!! усложните задачу, "отловив" и обработав исключение,
придумайте как это сделать
"""
import re

def has_cyrillic(text):
    return bool(re.search('[а-яА-Я]', text))

data = ['attribute', 'класс', 'функция', 'type']

for i in data:
    try:
        if has_cyrillic(i):
            raise Exception
        else: 
            print(f"Слово {i} можно записать в байтовом типе.")
    except Exception:
        print(f"ошибка: SyntaxError: bytes can only contain ASCII literal characters для слова {i}.")
     
