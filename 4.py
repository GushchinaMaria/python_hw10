"""
Задание 4.

Преобразовать слова «разработка», «администрирование», «protocol»,
«standard» из строкового представления в байтовое и выполнить
обратное преобразование (используя методы encode и decode).

Подсказки:
--- используйте списки и циклы, не дублируйте функции
"""
import chardet
data = ['разработка', 'администрирование', 'protocol', 'standard']
data_b = list()

for i in data:
    i_b = i.encode('utf-8')
    data_b.append(i_b)

print(f"Список слов в байтовом представлении: {data_b}")

res_data = list()

for i in data_b:
    i_b = i.decode('utf-8')
    res_data.append(i_b)

print(f"Список слов после обратного преобразования: {res_data}")