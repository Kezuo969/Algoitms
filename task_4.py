"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"

Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница, если нет, то вносит ее в кэш

Подсказка: задачу решите обязательно с применением 'соленого' хеширования
Можете условжнить задачу, реализовав ее через ООП
"""

from uuid import uuid4
import hashlib

salt = uuid4().hex  
obj = {}


def site(url):
    if obj.get(url):
        print(f' Этот сайт уже есть в кэше {url}')
    else:
        res = hashlib.sha256(salt.encode() + url.encode()).hexdigest()
        obj[url] = res
        print(obj)


get_page('https://geekbrains.ru/')
get_page('https://geekbrains.ru/')
