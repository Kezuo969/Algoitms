"""
Задание 3.
Определить количество различных подстрок с использованием хеш-функции.
Дана строка S длиной N, состоящая только из строчных латинских букв.

Подсказка: примените хеши и множества

рара:

рар
ра
ар
ара
р
а
"""
s = ["Papa"]
r = set()
n = len(s)
    for i in range(n):
        if i == 0:
            n = len(s) - 1
        else:
            n = len(s)
        for j in range(N, i, -1):
            print(s[i:j])
        
            r.add(hashlib.sha1(s[i:j].encode('utf-8')).hexdigest())
print(r)
