"""
Задание 3.
Определить количество различных (уникальных) подстрок
с использованием хеш-функции
Дана строка S длиной N, состоящая только из строчных латинских букв

Подсказка: вы должны в цикле для каждой подстроки вычислить хеш
Все хеши записываем во множество.
Оно отсечет дубли.

Экономия на размере хранимых данных (для длинных строк) и
скорость доступа вместе с уникальностью элементов,
которые даёт множество, сделают решение коротким и эффективным.

Пример:
рара - 6 уникальных подстрок

рар
ра
ар
ара
р
а
"""
import hashlib


def hash_uniq(word):
    my_set = set()
    my_hashset = set()
    for i in range(len(word)):
        for j in range(i+1, len(word)+1):
            my_str = word[i: j]
            my_set.add(my_str)
            my_hashset.add((hashlib.sha256(my_str[i:j].encode()).hexdigest()))
    print('В строке', word, len(my_set), 'уникальных элементов', '\n', my_hashset)


hash_uniq('papapa')
