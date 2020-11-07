"""
Задание 1.

Приведен код, который позволяет сохранить в
массиве индексы четных элементов другого массива

Сделайте замеры времени выполнения кода с помощью модуля timeit

Попробуйте оптимизировать код, чтобы снизить время выполнения
Проведите повторные замеры

Добавьте аналитику: что вы сделали и почему
"""


import timeit


def func_1(nums):
    """По нотации О большое- линейная сложность"""
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


def func_2(nums):
    """По нотации О большое- линейная сложность"""
    return [i for i, el in enum(nums) if el % 2 == 0]


nums = [i for i in range(10000)]

print(
    timeit.timeit(
        "func_1(nums)",
        setup="from __main__ import func_1, nums",
        number=10000))

nums = [i for i in range(10000)]
print(
    timeit.timeit(
        "func_2(NUMS)",
        setup="from __main__ import func_2, nums",
        number=10000))

Генераторное выражение эффективнее, поскольку выполняется быстрее цикла for


