"""
МОДУЛЬ 2
Программа из 2-го дз
Сначала пользователь вводит год рождения Пушкина, когда отвечает верно вводит день рождения
Можно использовать свой вариант программы из предыдущего дз, мой вариант реализован ниже
Задание: переписать код используя как минимум 1 функцию
"""

def ask_question(question, correct_answer):
    data = input(question)
    while data != correct_answer:
        print("Не верно")
        data = input(question)

ask_question('Ввведите год рождения А.С.Пушкина:', '1799')
ask_question('Ввведите день рождения А.С.Пушкина:', '6')

print('Верно')