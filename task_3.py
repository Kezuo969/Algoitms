"""
Задание 3.

Приведен код, формирующий из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран.

Сделайте профилировку каждого алгоритма через cProfile и через timeit

Сделайте вывод, какая из трех реализаций эффективнее и почему
"""
import cProfile
import timeit

def revers(enter_num, revers_num=0):
    if enter_num == 0:
        return
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        revers(enter_num, revers_num)


def revers_2(enter_num, revers_num=0):
    while enter_num != 0:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
    return revers_num


def revers_3(enter_num):
    enter_num = str(enter_num)
    revers_num = enter_num[::-1]
    return revers_num

cProfile.run('revers(90000000000)')
cProfile.run('revers_2(90000000000)')
cProfile.run('revers_3(90000000000)')

print('замер времени рекурсия: ', timeit(f'revers({enter_num})', setup='from __main__ import revers', number=10000))
print('замер времени цикле: ', timeit(f'revers_2({enter_num})', setup='from __main__ import revers_2', number=10000))
print('замер времени срезе: ', timeit(f'revers_3({enter_num})', setup='from __main__ import revers_3', number=10000))

"""Оптимально, в такого рода задачах, использовать срез ввиду выигрыша по времени обработки операции. 
У решений на циклах и рекурсии есть дополнительные арифметиеские операции.""" 