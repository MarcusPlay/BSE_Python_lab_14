#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Составить программу с использованием замыканий для решения задачи. 
# Вариант 12. Используя замыкания функций, объявите внутреннюю функцию, 
# которая заключает строку s (s – строка, параметр внутренней функции) в произвольный тег, 
# содержащийся в переменной tag – параметре внешней функции. Далее, 
# на вход программы поступает две строки: первая с тегом, вторая с некоторым содержимым. 
# Вторую строку нужно поместить в тег из первой строки с помощью реализованного замыкания. 
# Результат выведите на экран.


def create_tagged_string(tag):
    def tag_string(content):
        return f"<{tag}>{content}</{tag}>"
    return tag_string


if __name__=="__main__":
    tag_input = input("Введите тег: ")
    content_input = input("Введите содержимое: ")

    tagged_string_closure = create_tagged_string(tag_input)
    result = tagged_string_closure(content_input)

    print("Результат:", result)
