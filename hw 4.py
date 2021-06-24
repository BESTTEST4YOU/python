# 1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
# В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
# Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.

from sys import argv
script_name, hours, rate_per_hour, bonus = argv
hours, rate_per_hour, bonus = map(int, argv[1:])
print("Salary: ", hours * rate_per_hour + bonus, "руб.")


# 2. Представлен список чисел. Необходимо вывести элементы исходного списка,
# значения которых больше предыдущего элемента.
# Подсказка: элементы, удовлетворяющие условию, оформить в виде списка.
# Для формирования списка использовать генератор.
# Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
# Результат: [12, 44, 4, 10, 78, 123].

import random
lst = [random.randrange(3, 33, 3) for i in range(15)]
new_lst = [number for i, number in enumerate(lst) if i > 0 and lst[i] > lst[i - 1]]
# print(f"Old list: {lst}")
print("New list: ", new_lst)


# 3. Для чисел в пределах от 20 до 240 найти числа, кратные 20 или 21.
# Необходимо решить задание в одну строку. # Подсказка: использовать функцию range() и генератор.

new = [i for i in range(20, 240) if i % 21 == 0]
# print(new)

# 4. Представлен список чисел. Определить элементы списка, не имеющие повторений.
# Сформировать итоговый массив чисел, соответствующих требованию.
# Элементы вывести в порядке их следования в исходном списке.
# Для выполнения задания обязательно использовать генератор.
# Пример исходного списка: [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11].
# Результат: [23, 1, 3, 10, 4, 11]

from itertools import count
lst = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
"""первый / не правильный вариант"""
# new_lst = []
# for i in lst:
#     if lst.count(i) == 1:
#         new_lst.append(i)

new_lst = []
for el in count():
    """тут если вставить lst будет ошибка на итерацию. если оставить так, то цикл вечный. как пройти список используя count?"""
    if el == 1 in lst.count(1):  
        new_lst.append(el)

print('first list: ', lst)
print('result list: ', new_lst)

"""c 5 завал полный"""
# 5. Реализовать формирование списка, используя функцию range() и возможности генератора.
# В список должны войти четные числа от 100 до 1000 (включая границы).
# Необходимо получить результат вычисления произведения всех элементов списка.
# Подсказка: использовать функцию reduce().


import math
from itertools import count
from random import randrange
from functools import reduce
def multiplication():
new = []
for el in count(100, 2):
    if el > 1000:
        break
    else:
        new.append(el)
        print(new)
multiplication() int

# print(reduce(multiplication, [i, b]))
# print(functools.reduce(lambda a, b : a * b, new))

    # lst1 = [randrange(99, 1001, 1)]
    # new = []
    # for i in lst1:
    #     i * (i+1)
    #     new.insert(i)
# print(reduce(multiplication, [a, b]))

# 5. Реализовать формирование списка, используя функцию range() и возможности генератора.
# В список должны войти четные числа от 100 до 1000 (включая границы).
# Необходимо получить результат вычисления произведения всех элементов списка.
# Подсказка: использовать функцию reduce().


import math
from itertools import count
from random import randrange
from functools import reduce
def multiplication():
new = []
for el in count(100, 2):
    if el > 1000:
        break
    else:
        new.append(el)
        print(new)
multiplication() int

# print(reduce(multiplication, [i, b]))
# print(functools.reduce(lambda a, b : a * b, new))

    # lst1 = [randrange(99, 1001, 1)]
    # new = []
    # for i in lst1:
    #     i * (i+1)
    #     new.insert(i)
# print(reduce(multiplication, [a, b]))

# 6. Реализовать два небольших скрипта:
# а) итератор, генерирующий целые числа, начиная с указанного,
# б) итератор, повторяющий элементы некоторого списка, определенного заранее.
# Подсказка: использовать функцию count() и cycle() модуля itertools.
# Обратите внимание, что создаваемый цикл не должен быть бесконечным.
# Необходимо предусмотреть условие его завершения.
# Например, в первом задании выводим целые числа, начиная с 3, а при достижении числа 10 завершаем цикл.
# Во втором также необходимо предусмотреть условие, при котором повторение элементов списка будет прекращено.


import time
from itertools import count

print('итератор "a"')
# i = int(input('>>>'))
i = int(2)
for el in count(i):
    if el == 6:
        break
    else:
        print(el)
        
time.sleep(2)

print('итератор "b"')
from itertools import cycle
lst = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
for el in cycle(lst):
    if el == 3:
        break
    else:
        print(el, end=" ")

# 7 (Дополнительно). Реализовать генератор с помощью функции с ключевым словом yield,
# создающим очередное значение. При вызове функции должен создаваться объект-генератор.
# Функция должна вызываться следующим образом: for el in fact(n).
# Функция отвечает за получение факториала числа,
# а в цикле необходимо выводить только первые n чисел, начиная с 1! и до n!.
# Подсказка: факториал числа n — произведение чисел от 1 до n. Например,
# факториал четырёх 4! = 1 * 2 * 3 * 4 = 24.

from itertools import count
from math import factorial
def gen():
    for i in count(1):
        yield factorial(i)
generator = gen()
x = 0
for k in generator:
    if x < 4:
        print(k)
        x += 1
    else:
        break
