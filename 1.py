"""
Задание 1.

Каждое из слов «разработка», «сокет», «декоратор» представить
в буквенном формате и проверить тип и содержание соответствующих переменных.
Затем с помощью онлайн-конвертера преобразовать
в набор кодовых точек Unicode (НО НЕ В БАЙТЫ!!!)
и также проверить тип и содержимое переменных.

Подсказки:
--- 'разработка' - буквенный формат
--- '\u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u043a\u0430' - набор кодовых точек
--- используйте списки и циклы, не дублируйте функции
"""

str_1 = "разработка"
str_2 = "сокет"
str_3 = "декоратор"


def Check_word(word):
    list_str_1 = []
    print(word)
    for el in word:
        list_str_1.append(el)
        print(f" Type of {el} : {type(el)}")


Check_word(str_1)
Check_word(str_2)
Check_word(str_3)


u_str_1 = "\u0440\u0430\u0437\u0440\u0430\u0431\u043E\u0442\u043A\u0430"
u_str_2 = "\u0441\u043E\u043A\u0435\u0442"
u_str_3 = "\u0434\u0435\u043A\u043E\u0440\u0430\u0442\u043E\u0440"

print(f"Type of '{u_str_1}': {type(u_str_1)}")
Check_word(u_str_1)
print(f"Type of '{u_str_2}': {type(u_str_2)}")
Check_word(u_str_2)
print(f"Type of '{u_str_3}': {type(u_str_3)}")
Check_word(u_str_3)