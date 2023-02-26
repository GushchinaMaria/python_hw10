"""
Задание 2.

Каждое из слов «class», «function», «method» записать в байтовом формате
без преобразования в последовательность кодов
не используя!!! методы encode и decode)
и определить тип, содержимое и длину соответствующих переменных.

Подсказки:
--- b'class' - используйте маркировку b''
--- используйте списки и циклы, не дублируйте функции
"""
w_1 = "class"
w_2 = "function"
w_3 = "method"

def Convert_to_bytes(word):
    b_w = bytes(word, 'utf-8')
    print(f"Type of {b_w} : {type(b_w)}")
    print(f"Lenght of {b_w} : {len(b_w)}")
    print(b_w)

    for el in b_w:
        print(f"Type of element {el} :{type(el)}")

Convert_to_bytes(w_1)
Convert_to_bytes(w_2)
Convert_to_bytes(w_3)