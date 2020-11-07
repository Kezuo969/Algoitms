"""
Задание 2.
Ваша программа должна запрашивать пароль
Для этого пароля вам нужно получить хеш, используя функцию sha256
Для генерации хеша обязательно нужно использовать криптографическую соль
Обязательно выведите созданный хеш

Далее программа должна запросить пароль повторно
Вам нужно проверить, совпадает ли пароль с исходным
Для проверки необходимо сравнить хеши паролей

ПРИМЕР:
Введите пароль: 123
В базе данных хранится строка: 555a3581d37993843efd4eba1921f1dcaeeafeb855965535d77c55782349444b
Введите пароль еще раз для проверки: 123
Вы ввели правильный пароль
"""
import hashlib
passw = hashlib.sha256(input("введите пароль"))

while passw != check:
    passw = hashlib.sha256(input("введите пароль"))
    print(passw)  
    print(type(hash_obj))  # -> <class '_hashlib.HASH'>
    res = passw.hexdigest()
    print(type(res))  # -> <class 'str'>
    print(res)  # -> b631e4f1254574b9c386fcbc9145d0c3
    check = hashlib.sha256(input("Повторите пароль для проверки"))

if res ==  

Python
import hashlib

salt = b'' # Получение соли, сохраненной для *этого* пользователя
key = b'' # Получение рассчитанного ключа пользователя

password_to_check = 'password246' # Пароль, предоставленный пользователем, проверяется

# Используется та же настройка для генерации ключа, только на этот раз вставляется для проверки настоящий пароль
new_key = hashlib.pbkdf2_hmac(
    'sha256',
    password_to_check.encode('utf-8'), # Конвертирование пароля в байты
    salt, 
    100000
)

if new_key == key:
    print('Пароль правильный')
else:
    print('Пароль неправильный')

import os
import hashlib
 
# Пример генерации
salt = os.urandom(32)
key = hashlib.pbkdf2_hmac('sha256', 'mypassword'.encode('utf-8'), salt, 100000)
 
# Хранение как
storage = salt + key 
 
# Получение значений обратно
salt_from_storage = storage[:32] # 32 является длиной соли
key_from_storage = storage[32:]
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
import hashlib
 
salt = b'user_id' # Получение соли, сохраненной для *этого* пользователя
key = input(b'') # Получение рассчитанного ключа пользователя
 
password_to_check = 'password246' # Пароль, предоставленный пользователем, проверяется
 
# Используется та же настройка для генерации ключа, только на этот раз вставляется для проверки настоящий пароль
new_key = hashlib.pbkdf2_hmac(
    'sha256',
    password_to_check.encode('utf-8'), # Конвертирование пароля в байты
    salt, 
    100000
)
 
if new_key == key:
    print('Пароль правильный')
else:
    print('Пароль неправильный')
