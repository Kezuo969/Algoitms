"""
1.	Написать программу, которая будет складывать, вычитать, умножать или делить
два числа. Числа и знак операции вводятся пользователем. После выполнения
вычисления программа не должна завершаться, а должна запрашивать новые данные
для вычислений. Завершение программы должно выполняться при вводе символа '0'
в качестве знака операции. Если пользователь вводит неверный знак
(не '0', '+', '-', '*', '/'), то программа должна сообщать ему об ошибке и
снова запрашивать знак операции.

Также сообщать пользователю о невозможности деления на ноль,
если он ввел 0 в качестве делителя.

Подсказка:
Вариант исполнения:
- условие рекурсивного вызова - введена операция +, -, *, / - ШАГ РЕКУРСИИ
- условие завершения рекурсии - введена операция 0 - БАЗОВЫЙ СЛУЧАЙ

Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7

Пример:
Введите операцию (+, -, *, / или 0 для выхода): +
Введите первое число: 214
Введите второе число: 234
Ваш результат 448
Введите операцию (+, -, *, / или 0 для выхода): -
Введите первое число: вп
Вы вместо трехзначного числа ввели строку (((. Исправьтесь
Введите операцию (+, -, *, / или 0 для выхода):
"""

class Script(Exception):
    def __init__(self, data, sheld):
        self.data = data
        sheld = []
        data = input("Enter number to exit enter 'stop'").lower()
        if data !="stop":
            if data.isdigit() == True:
                sheld.append(data)
                data = input("Enter number to exit enter 'stop'")



def menu():
    print ("Welcome to calculator.py")
    print ("your options are:") pr
    int (" ") print ("1) Addition")
    print ("2) Subtraction")
    print ("3) Multiplication")
    print ("4) Division")
    print ("5) Quit calculator.py")
    print (" ")
    return input ("Choose your option: ")

    def add(a,b): print (a, "+", b, "=", a + b)
    def sub(a,b): print (b, "-", a, "=", b - a)
    def mul(a,b): print (a, "*", b, "=", a * b)
    def div(a,b): print (a, "/", b, "=", a / b) loop = 1 choice = 0
    while loop == 1: choice = menu()
    if choice == 1: add(input("Add this: "),input("to this: "))
    elif choice == 2: sub(input("Subtract this: "),input("from this: "))
    elif choice == 3: mul(input("Multiply this: "),input("by this: "))
    elif choice == 4: div(input("Divide this: "),input("by this: "))
    elif choice == 5: loop = 0 print ("Thank you for using calculator.py!")